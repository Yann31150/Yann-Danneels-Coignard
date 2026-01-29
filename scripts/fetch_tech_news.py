#!/usr/bin/env python3
"""
Script pour récupérer les actualités tech quotidiennes
Utilise NewsAPI et filtre les articles pertinents avec des mots-clés
"""

import json
import os
import requests
from datetime import datetime, timedelta
from typing import List, Dict
import sys

# Configuration
NEWS_API_KEY = os.getenv('NEWS_API_KEY', '')  # À configurer dans GitHub Secrets
OUTPUT_FILE = 'docs/tech-news.json'

# Mots-clés pour filtrer les articles pertinents
TECH_KEYWORDS = [
    'artificial intelligence', 'machine learning', 'deep learning', 'neural network',
    'data science', 'data analyst', 'big data', 'analytics',
    'python', 'sql', 'power bi', 'tableau', 'pandas', 'numpy',
    'cloud computing', 'aws', 'azure', 'gcp',
    'startup', 'innovation', 'tech', 'technology',
    'blockchain', 'cryptocurrency', 'web3',
    'cybersecurity', 'privacy', 'gdpr',
    'automation', 'robotics', 'iot', 'internet of things'
]

FRENCH_KEYWORDS = [
    'intelligence artificielle', 'apprentissage automatique', 'science des données',
    'analyse de données', 'données', 'big data',
    'innovation', 'technologie', 'startup',
    'cybersécurité', 'cloud', 'automatisation'
]

def fetch_news_from_api() -> List[Dict]:
    """Récupère les articles depuis NewsAPI"""
    articles = []
    
    if not NEWS_API_KEY:
        print("⚠️  NEWS_API_KEY non configurée. Utilisation de données d'exemple.")
        return get_example_articles()
    
    # Rechercher en anglais
    for keyword in TECH_KEYWORDS[:5]:  # Limiter pour éviter trop de requêtes
        try:
            url = 'https://newsapi.org/v2/everything'
            params = {
                'q': keyword,
                'language': 'en',
                'sortBy': 'publishedAt',
                'pageSize': 5,
                'from': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),
                'apiKey': NEWS_API_KEY
            }
            
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                articles.extend(data.get('articles', []))
        except Exception as e:
            print(f"Erreur lors de la récupération pour '{keyword}': {e}")
    
    # Rechercher en français
    for keyword in FRENCH_KEYWORDS[:3]:
        try:
            url = 'https://newsapi.org/v2/everything'
            params = {
                'q': keyword,
                'language': 'fr',
                'sortBy': 'publishedAt',
                'pageSize': 5,
                'from': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),
                'apiKey': NEWS_API_KEY
            }
            
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                articles.extend(data.get('articles', []))
        except Exception as e:
            print(f"Erreur lors de la récupération pour '{keyword}': {e}")
    
    return articles

def get_example_articles() -> List[Dict]:
    """Retourne des articles d'exemple si l'API n'est pas disponible"""
    return [
        {
            'title': 'Les tendances de l\'IA en 2026',
            'description': 'Découvrez les dernières innovations en intelligence artificielle et leur impact sur le monde de la data. L\'intelligence artificielle continue de transformer les entreprises et les métiers de la data.',
            'url': 'https://example.com/ai-trends-2026',
            'source': {'name': 'Tech News'},
            'publishedAt': datetime.now().isoformat(),
            'category': 'ai'
        },
        {
            'title': 'Power BI : Nouvelles fonctionnalités',
            'description': 'Microsoft annonce de nouvelles fonctionnalités pour Power BI qui facilitent l\'analyse de données et la visualisation pour les data analysts.',
            'url': 'https://example.com/power-bi-updates',
            'source': {'name': 'Data Weekly'},
            'publishedAt': (datetime.now() - timedelta(hours=5)).isoformat(),
            'category': 'data'
        },
        {
            'title': 'Python et Data Science : Les outils essentiels',
            'description': 'Un aperçu des bibliothèques Python les plus utilisées en data science : Pandas, NumPy, et Scikit-learn pour l\'analyse de données.',
            'url': 'https://example.com/python-data-science',
            'source': {'name': 'Tech Innovation'},
            'publishedAt': (datetime.now() - timedelta(hours=10)).isoformat(),
            'category': 'data'
        }
    ]

def filter_and_process_articles(raw_articles: List[Dict]) -> List[Dict]:
    """Filtre et traite les articles pour ne garder que les plus pertinents"""
    processed = []
    seen_titles = set()
    
    for article in raw_articles:
        title = article.get('title', '').lower()
        
        # Éviter les doublons
        if title in seen_titles:
            continue
        seen_titles.add(title)
        
        # Filtrer par mots-clés
        content = (title + ' ' + article.get('description', '')).lower()
        is_relevant = any(keyword.lower() in content for keyword in TECH_KEYWORDS + FRENCH_KEYWORDS)
        
        if not is_relevant:
            continue
        
        # Déterminer la catégorie
        category = 'tech'
        if any(kw in content for kw in ['ai', 'artificial intelligence', 'machine learning', 'intelligence artificielle']):
            category = 'ai'
        elif any(kw in content for kw in ['data', 'analytics', 'big data', 'données']):
            category = 'data'
        elif any(kw in content for kw in ['innovation', 'startup', 'nouveau']):
            category = 'innovation'
        
        # Vérifier s'il y a une vidéo (basé sur l'URL ou le contenu)
        has_video = 'video' in content or 'youtube' in article.get('url', '').lower() or 'vimeo' in article.get('url', '').lower()
        
        processed.append({
            'title': article.get('title', 'Sans titre'),
            'description': article.get('description', '')[:200] + '...' if len(article.get('description', '')) > 200 else article.get('description', ''),
            'url': article.get('url', '#'),
            'source': article.get('source', {}).get('name', 'Source inconnue') if isinstance(article.get('source'), dict) else article.get('source', 'Source inconnue'),
            'publishedAt': article.get('publishedAt', datetime.now().isoformat()),
            'category': category,
            'hasVideo': has_video
        })
    
    # Trier par date (plus récent en premier) et limiter à 20 articles
    processed.sort(key=lambda x: x['publishedAt'], reverse=True)
    return processed[:20]

def save_articles(articles: List[Dict]):
    """Sauvegarde les articles dans le fichier JSON"""
    output_data = {
        'lastUpdate': datetime.now().isoformat(),
        'articles': articles
    }
    
    # Créer le dossier si nécessaire
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ {len(articles)} articles sauvegardés dans {OUTPUT_FILE}")

def main():
    try:
        print("🚀 Récupération des actualités tech...")
        
        # Récupérer les articles
        raw_articles = fetch_news_from_api()
        print(f"📰 {len(raw_articles)} articles récupérés")
        
        # Filtrer et traiter
        processed_articles = filter_and_process_articles(raw_articles)
        print(f"✨ {len(processed_articles)} articles pertinents sélectionnés")
        
        # S'assurer qu'on a au moins quelques articles
        if len(processed_articles) == 0:
            print("⚠️  Aucun article trouvé, utilisation d'articles d'exemple")
            example_articles = get_example_articles()
            processed_articles = filter_and_process_articles(example_articles)
        
        # Sauvegarder
        save_articles(processed_articles)
        
        print("✅ Terminé !")
        return 0
    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        # En cas d'erreur, sauvegarder au moins les articles d'exemple
        try:
            example_articles = get_example_articles()
            processed_articles = filter_and_process_articles(example_articles)
            save_articles(processed_articles)
            print("✅ Articles d'exemple sauvegardés en cas d'erreur")
        except:
            pass
        return 1

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
