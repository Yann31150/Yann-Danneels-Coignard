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

# Mots-clés français prioritaires (Data et IA en premier)
FRENCH_KEYWORDS_DATA_AI = [
    'intelligence artificielle', 'IA', 'apprentissage automatique', 'machine learning',
    'science des données', 'data science', 'analyse de données', 'data analyst',
    'big data', 'données', 'analytics', 'business intelligence',
    'power bi', 'tableau', 'python', 'sql', 'pandas', 'numpy',
    'visualisation de données', 'tableau de bord', 'data visualization'
]

FRENCH_KEYWORDS_GENERAL = [
    'innovation', 'technologie', 'startup tech',
    'cybersécurité', 'cloud computing', 'automatisation'
]

def fetch_news_from_api() -> List[Dict]:
    """Récupère les articles depuis NewsAPI - Priorité aux articles français sur Data et IA"""
    articles = []
    
    if not NEWS_API_KEY:
        print("⚠️  NEWS_API_KEY non configurée. Utilisation de données d'exemple.")
        return get_example_articles()
    
    # PRIORITÉ 1 : Rechercher en français - Data et IA (plus de requêtes)
    print("🔍 Recherche d'articles français sur Data et IA...")
    for keyword in FRENCH_KEYWORDS_DATA_AI[:8]:  # Plus de mots-clés pour Data/IA
        try:
            url = 'https://newsapi.org/v2/everything'
            params = {
                'q': keyword,
                'language': 'fr',
                'sortBy': 'publishedAt',
                'pageSize': 8,  # Plus d'articles par requête
                'from': (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d'),  # 2 jours au lieu de 1
                'apiKey': NEWS_API_KEY
            }
            
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                fetched = data.get('articles', [])
                articles.extend(fetched)
                print(f"  ✓ {len(fetched)} articles trouvés pour '{keyword}'")
            elif response.status_code == 429:
                print(f"  ⚠️  Limite de taux atteinte pour '{keyword}'")
        except Exception as e:
            print(f"  ❌ Erreur pour '{keyword}': {e}")
    
    # PRIORITÉ 2 : Rechercher en français - Général (moins de requêtes)
    print("🔍 Recherche d'articles français généraux...")
    for keyword in FRENCH_KEYWORDS_GENERAL[:3]:
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
                fetched = data.get('articles', [])
                articles.extend(fetched)
                print(f"  ✓ {len(fetched)} articles trouvés pour '{keyword}'")
            elif response.status_code == 429:
                print(f"  ⚠️  Limite de taux atteinte pour '{keyword}'")
        except Exception as e:
            print(f"  ❌ Erreur pour '{keyword}': {e}")
    
    # PRIORITÉ 3 : Rechercher en anglais uniquement si pas assez d'articles français
    if len(articles) < 10:
        print("🔍 Complément avec articles anglais sur Data et IA...")
        for keyword in ['artificial intelligence', 'data science', 'machine learning', 'data analytics'][:3]:
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
                print(f"  ❌ Erreur pour '{keyword}': {e}")
    
    return articles

def get_example_articles() -> List[Dict]:
    """Retourne des articles d'exemple en français sur Data et IA si l'API n'est pas disponible"""
    return [
        {
            'title': 'Intelligence Artificielle : Les tendances 2026 pour les data analysts',
            'description': 'Découvrez les dernières innovations en intelligence artificielle et leur impact sur le monde de la data. L\'IA continue de transformer les entreprises et les métiers de l\'analyse de données.',
            'url': 'https://example.com/ai-trends-2026',
            'source': {'name': 'Data News France'},
            'publishedAt': datetime.now().isoformat(),
            'category': 'ai'
        },
        {
            'title': 'Power BI : Nouvelles fonctionnalités pour l\'analyse de données',
            'description': 'Microsoft annonce de nouvelles fonctionnalités pour Power BI qui facilitent l\'analyse de données et la visualisation pour les data analysts. Des outils plus puissants pour transformer vos données en insights.',
            'url': 'https://example.com/power-bi-updates',
            'source': {'name': 'Data Weekly France'},
            'publishedAt': (datetime.now() - timedelta(hours=5)).isoformat(),
            'category': 'data'
        },
        {
            'title': 'Python et Data Science : Les bibliothèques essentielles',
            'description': 'Un guide complet des bibliothèques Python les plus utilisées en data science : Pandas pour la manipulation de données, NumPy pour le calcul scientifique, et Scikit-learn pour le machine learning.',
            'url': 'https://example.com/python-data-science',
            'source': {'name': 'Tech Innovation France'},
            'publishedAt': (datetime.now() - timedelta(hours=10)).isoformat(),
            'category': 'data'
        },
        {
            'title': 'Machine Learning : Comment l\'IA révolutionne l\'analyse de données',
            'description': 'L\'apprentissage automatique transforme la façon dont les entreprises analysent leurs données. Découvrez comment les algorithmes de machine learning permettent d\'extraire des insights précieux.',
            'url': 'https://example.com/ml-data-analysis',
            'source': {'name': 'IA Magazine'},
            'publishedAt': (datetime.now() - timedelta(hours=15)).isoformat(),
            'category': 'ai'
        },
        {
            'title': 'Big Data et Analytics : Les défis de 2026',
            'description': 'Face à l\'explosion du volume de données, les entreprises doivent adopter de nouvelles stratégies d\'analyse. Découvrez les tendances du big data et de l\'analytics pour cette année.',
            'url': 'https://example.com/big-data-analytics',
            'source': {'name': 'Data Insights'},
            'publishedAt': (datetime.now() - timedelta(hours=20)).isoformat(),
            'category': 'data'
        }
    ]

def filter_and_process_articles(raw_articles: List[Dict]) -> List[Dict]:
    """Filtre et traite les articles pour ne garder que les plus pertinents"""
    processed = []
    seen_titles = set()
    
    for article in raw_articles:
        # Récupérer et nettoyer les valeurs (gérer les None)
        title = str(article.get('title') or '').strip()
        description = str(article.get('description') or '').strip()
        url = str(article.get('url') or '#').strip()
        
        # Ignorer les articles sans titre
        if not title:
            continue
        
        title_lower = title.lower()
        
        # Éviter les doublons
        if title_lower in seen_titles:
            continue
        seen_titles.add(title_lower)
        
        # Filtrer par mots-clés (priorité aux mots-clés français Data/IA)
        content = (title_lower + ' ' + description.lower()).lower()
        all_keywords = FRENCH_KEYWORDS_DATA_AI + FRENCH_KEYWORDS_GENERAL + TECH_KEYWORDS
        is_relevant = any(keyword.lower() in content for keyword in all_keywords)
        
        if not is_relevant:
            continue
        
        # Calculer un score de pertinence (priorité Data et IA)
        relevance_score = 0
        data_ai_keywords_fr = ['intelligence artificielle', 'ia', 'apprentissage automatique', 
                               'science des données', 'data science', 'analyse de données', 
                               'data analyst', 'big data', 'données', 'analytics', 
                               'business intelligence', 'power bi', 'tableau', 'python', 'sql']
        data_ai_keywords_en = ['artificial intelligence', 'ai', 'machine learning', 
                               'data science', 'data analyst', 'big data', 'analytics']
        
        # Bonus pour les articles français
        if any(kw in content for kw in FRENCH_KEYWORDS_DATA_AI):
            relevance_score += 10
        
        # Bonus pour Data et IA
        if any(kw in content for kw in data_ai_keywords_fr + data_ai_keywords_en):
            relevance_score += 5
        
        # Déterminer la catégorie (priorité Data et IA)
        category = 'tech'
        ai_keywords = ['ai', 'artificial intelligence', 'machine learning', 'deep learning',
                       'intelligence artificielle', 'apprentissage automatique', 'neural network']
        data_keywords = ['data', 'analytics', 'big data', 'données', 'data science', 
                        'science des données', 'analyse de données', 'data analyst',
                        'power bi', 'tableau', 'business intelligence', 'visualisation']
        
        if any(kw in content for kw in ai_keywords):
            category = 'ai'
            relevance_score += 3
        elif any(kw in content for kw in data_keywords):
            category = 'data'
            relevance_score += 3
        elif any(kw in content for kw in ['innovation', 'startup', 'nouveau']):
            category = 'innovation'
        
        # Ajouter le score de pertinence à l'article pour le tri
        article['_relevance_score'] = relevance_score
        
        # Vérifier s'il y a une vidéo (basé sur l'URL ou le contenu)
        url_lower = url.lower()
        has_video = 'video' in content or 'youtube' in url_lower or 'vimeo' in url_lower
        
        # Traiter la source
        source_obj = article.get('source')
        if isinstance(source_obj, dict):
            source_name = source_obj.get('name', 'Source inconnue')
        elif isinstance(source_obj, str):
            source_name = source_obj
        else:
            source_name = 'Source inconnue'
        
        # Traiter la description (limiter à 200 caractères)
        description_short = description[:200] + '...' if len(description) > 200 else description
        
        processed.append({
            'title': title,
            'description': description_short,
            'url': url,
            'source': source_name,
            'publishedAt': article.get('publishedAt') or datetime.now().isoformat(),
            'category': category,
            'hasVideo': has_video,
            '_relevance_score': article.get('_relevance_score', 0)
        })
    
    # Trier par score de pertinence (Data/IA en premier), puis par date
    processed.sort(key=lambda x: (-x['_relevance_score'], x['publishedAt']), reverse=True)
    
    # Retirer le score de pertinence avant de retourner
    for article in processed:
        article.pop('_relevance_score', None)
    
    return processed[:25]  # Plus d'articles pour avoir plus de choix

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
