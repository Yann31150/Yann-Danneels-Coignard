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
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY', '')  # À configurer dans GitHub Secrets
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

def fetch_youtube_videos() -> List[Dict]:
    """Récupère des vidéos YouTube pertinentes sur la tech, data et IA"""
    videos = []
    
    if not YOUTUBE_API_KEY:
        print("⚠️  YOUTUBE_API_KEY non configurée. Pas de vidéos YouTube.")
        return []
    
    # Recherches YouTube pour Data et IA
    search_queries = [
        'intelligence artificielle français',
        'data science français',
        'machine learning français',
        'power bi tutorial français',
        'python data analysis français',
        'sql tutorial français'
    ]
    
    for query in search_queries[:4]:  # Limiter à 4 requêtes pour éviter les quotas
        try:
            url = 'https://www.googleapis.com/youtube/v3/search'
            params = {
                'part': 'snippet',
                'q': query,
                'type': 'video',
                'maxResults': 3,  # Réduire pour éviter les quotas
                'order': 'relevance',
                'relevanceLanguage': 'fr',
                'publishedAfter': (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%dT%H:%M:%SZ'),
                'key': YOUTUBE_API_KEY
            }
            
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                items = data.get('items', [])
                for item in items:
                    try:
                        snippet = item.get('snippet', {})
                        video_id_obj = item.get('id', {})
                        video_id = video_id_obj.get('videoId', '') if isinstance(video_id_obj, dict) else ''
                        
                        if video_id:
                            thumbnails = snippet.get('thumbnails', {})
                            thumbnail_url = ''
                            if isinstance(thumbnails, dict):
                                high_thumb = thumbnails.get('high', {})
                                thumbnail_url = high_thumb.get('url', '') if isinstance(high_thumb, dict) else ''
                            
                            videos.append({
                                'title': str(snippet.get('title', '')),
                                'description': str(snippet.get('description', '')),
                                'url': f'https://www.youtube.com/watch?v={video_id}',
                                'source': str(snippet.get('channelTitle', 'YouTube')),
                                'publishedAt': str(snippet.get('publishedAt', datetime.now().isoformat())),
                                'thumbnail': thumbnail_url,
                                'videoId': video_id,
                                'isYouTube': True
                            })
                    except Exception as e:
                        print(f"    ⚠️  Erreur traitement vidéo: {e}")
                        continue
                        
                print(f"  ✓ {len(items)} vidéos trouvées pour '{query}'")
            elif response.status_code == 403:
                print(f"  ⚠️  Quota YouTube API dépassé ou clé invalide pour '{query}'")
                break
            elif response.status_code == 400:
                print(f"  ⚠️  Requête YouTube invalide pour '{query}'")
                continue
            else:
                print(f"  ⚠️  Erreur YouTube API (code {response.status_code}) pour '{query}'")
        except requests.exceptions.Timeout:
            print(f"  ⚠️  Timeout pour '{query}'")
            continue
        except Exception as e:
            print(f"  ❌ Erreur YouTube pour '{query}': {e}")
            continue
    
    return videos

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
    """Filtre et traite les articles pour ne garder que les plus pertinents avec catégorisation stricte"""
    processed = []
    seen_titles = set()
    
    # Mots-clés STRICTS pour l'IA - Version renforcée avec combinaisons obligatoires
    # Pour être catégorisé en IA, l'article doit contenir au moins 2 de ces termes
    STRICT_AI_KEYWORDS_PRIMARY = [
        'intelligence artificielle', 'artificial intelligence',
        'machine learning', 'apprentissage automatique',
        'deep learning', 'apprentissage profond',
        'neural network', 'réseau de neurones',
        'chatgpt', 'gpt-', 'gpt ', 'llm', 'large language model', 'modèle de langage',
        'transformer', 'reinforcement learning', 'apprentissage par renforcement',
        'computer vision', 'vision par ordinateur',
        'nlp', 'traitement du langage naturel', 'natural language processing'
    ]
    
    STRICT_AI_KEYWORDS_SECONDARY = [
        'ia', 'ai ', 'ai,', 'ai.', 'ai:', 'ai;',  # "ai" seul peut être ambigu
        'algorithm', 'algorithme', 'modèle', 'model',
        'entraînement', 'training', 'dataset', 'jeu de données'
    ]
    
    # Combinaisons qui garantissent que c'est vraiment sur l'IA
    AI_REQUIRED_COMBINATIONS = [
        ['intelligence artificielle', 'machine learning'],
        ['artificial intelligence', 'neural'],
        ['deep learning', 'réseau'],
        ['chatgpt', 'ia'],
        ['gpt', 'intelligence'],
        ['llm', 'artificielle'],
        ['transformer', 'learning'],
        ['computer vision', 'ai']
    ]
    
    # Mots-clés STRICTS pour la Data (doivent être présents pour catégoriser en Data)
    STRICT_DATA_KEYWORDS = [
        'data science', 'science des données', 'data analyst', 'analyste de données',
        'analyse de données', 'data analysis', 'big data', 'données',
        'analytics', 'business intelligence', 'bi', 'intelligence d\'affaires',
        'power bi', 'tableau', 'visualisation de données', 'data visualization',
        'sql', 'python data', 'pandas', 'numpy', 'data mining', 'fouille de données',
        'data warehouse', 'entrepôt de données', 'etl', 'extract transform load'
    ]
    
    # Mots d'exclusion pour éviter les faux positifs
    EXCLUSION_KEYWORDS = [
        'sport', 'football', 'soccer', 'basketball', 'tennis', 'jeux olympiques',
        'politique', 'élection', 'vote', 'gouvernement', 'ministre', 'président',
        'crypto', 'bitcoin', 'blockchain', 'nft'  # Exclure crypto sauf si combiné avec data/ia
    ]
    
    for article in raw_articles:
        # Récupérer et nettoyer les valeurs (gérer les None)
        title = str(article.get('title') or '').strip()
        description = str(article.get('description') or '').strip()
        url = str(article.get('url') or '#').strip()
        
        # Ignorer les articles sans titre
        if not title:
            continue
        
        title_lower = title.lower()
        description_lower = description.lower()
        url_lower = url.lower()
        content = (title_lower + ' ' + description_lower).lower()
        
        # Vérifier si c'est une vidéo YouTube (elles passent automatiquement le filtre)
        is_youtube_video = article.get('isYouTube', False) or 'youtube.com' in url_lower or 'youtu.be' in url_lower
        
        # Éviter les doublons
        if title_lower in seen_titles:
            continue
        seen_titles.add(title_lower)
        
        # EXCLURE les articles avec des mots-clés non pertinents (sauf si vraiment liés à data/ia ou vidéo YouTube)
        if not is_youtube_video:
            has_exclusion = any(excl in content for excl in EXCLUSION_KEYWORDS)
            has_data_ai = any(kw in content for kw in STRICT_AI_KEYWORDS_PRIMARY + STRICT_DATA_KEYWORDS)
            
            # Si contient des mots d'exclusion ET pas de mots data/ia, exclure
            if has_exclusion and not has_data_ai:
                continue
        
        # Vérifier la pertinence générale (sauf pour les vidéos YouTube qui sont toujours pertinentes)
        if not is_youtube_video:
            all_keywords = FRENCH_KEYWORDS_DATA_AI + FRENCH_KEYWORDS_GENERAL + TECH_KEYWORDS
            is_relevant = any(keyword.lower() in content for keyword in all_keywords)
            
            if not is_relevant:
                continue
        else:
            # Les vidéos YouTube sont toujours considérées comme pertinentes
            is_relevant = True
        
        # Calculer un score de pertinence strict avec validation renforcée pour l'IA
        relevance_score = 0
        ai_score = 0
        data_score = 0
        
        # Compter les occurrences de mots-clés IA PRIMAIRES (score élevé)
        primary_ai_count = 0
        for kw in STRICT_AI_KEYWORDS_PRIMARY:
            count = content.count(kw.lower())
            if count > 0:
                primary_ai_count += count
                ai_score += count * 10  # Score très élevé pour les mots-clés primaires
                relevance_score += count * 10
        
        # Compter les occurrences de mots-clés IA SECONDAIRES (score moyen)
        secondary_ai_count = 0
        for kw in STRICT_AI_KEYWORDS_SECONDARY:
            count = content.count(kw.lower())
            if count > 0:
                secondary_ai_count += count
                ai_score += count * 2  # Score moyen pour les mots-clés secondaires
                relevance_score += count * 2
        
        # VALIDATION RENFORCÉE : Vérifier les combinaisons obligatoires
        has_ai_combination = False
        for combo in AI_REQUIRED_COMBINATIONS:
            if all(term.lower() in content for term in combo):
                has_ai_combination = True
                ai_score += 20  # Bonus important pour les combinaisons
                relevance_score += 20
                break
        
        # Pour être vraiment catégorisé en IA, il faut :
        # - Soit au moins 2 mots-clés primaires
        # - Soit 1 mot-clé primaire + 1 combinaison valide
        # - Soit une combinaison obligatoire
        is_really_ai = (primary_ai_count >= 2) or (primary_ai_count >= 1 and has_ai_combination) or has_ai_combination
        
        # Compter les occurrences de mots-clés Data STRICTS
        for kw in STRICT_DATA_KEYWORDS:
            count = content.count(kw.lower())
            if count > 0:
                data_score += count * 5  # Score élevé pour chaque occurrence
                relevance_score += count * 5
        
        # Bonus pour les articles français
        if any(kw in content for kw in FRENCH_KEYWORDS_DATA_AI):
            relevance_score += 3
        
        # Déterminer la catégorie de manière TRÈS STRICTE
        category = 'tech'
        
        # Pour être catégorisé en IA : validation renforcée obligatoire
        if is_really_ai and ai_score >= 10 and ai_score >= data_score:
            # Article vraiment sur l'IA (validation renforcée passée)
            category = 'ai'
            relevance_score += 15  # Bonus pour catégorie IA validée
        elif data_score >= 5 and data_score > ai_score:
            # Article vraiment sur la Data
            category = 'data'
            relevance_score += 10  # Bonus pour catégorie Data
        elif ai_score > 0 and data_score > 0:
            # Article mixte IA + Data, priorité à celui avec le score le plus élevé
            if ai_score >= data_score:
                category = 'ai'
            else:
                category = 'data'
            relevance_score += 8
        elif any(kw in content for kw in ['innovation', 'startup tech', 'technologie']):
            category = 'innovation'
        
        # Ne garder que les articles avec un score minimum (évite les faux positifs)
        # SAUF les vidéos YouTube qui sont toujours acceptées
        if not is_youtube_video and relevance_score < 3:
            continue
        
        # Pour les vidéos YouTube, donner un score minimum pour qu'elles passent
        if is_youtube_video and relevance_score < 3:
            relevance_score = 5  # Score minimum pour les vidéos YouTube
        
        # Ajouter le score de pertinence à l'article pour le tri
        article['_relevance_score'] = relevance_score
        article['_ai_score'] = ai_score
        article['_data_score'] = data_score
        
        # Vérifier s'il y a une vidéo (basé sur l'URL ou le contenu)
        # Note: is_youtube_video est déjà défini plus haut dans la fonction
        url_lower = url.lower()
        is_youtube = is_youtube_video  # Utiliser la variable déjà définie
        has_video = is_youtube or 'video' in content or 'vimeo' in url_lower
        video_id = article.get('videoId', '') if is_youtube else ''
        thumbnail = article.get('thumbnail', '') if is_youtube else ''
        
        # Pour les vidéos YouTube, déterminer la catégorie basée sur le titre/description
        if is_youtube:
            content_lower = content.lower()
            if any(kw in content_lower for kw in ['intelligence artificielle', 'ia', 'ai', 'machine learning', 'apprentissage automatique']):
                category = 'ai'
                relevance_score += 10
            elif any(kw in content_lower for kw in ['data', 'données', 'data science', 'science des données', 'power bi', 'tableau', 'sql', 'python']):
                category = 'data'
                relevance_score += 10
            else:
                category = 'tech'
                relevance_score += 5
        
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
            'hasVideo': has_video or is_youtube,
            'isYouTube': is_youtube,
            'videoId': video_id,
            'thumbnail': thumbnail,
            '_relevance_score': article.get('_relevance_score', 0),
            '_ai_score': article.get('_ai_score', 0),
            '_data_score': article.get('_data_score', 0)
        })
    
    # Trier par score de pertinence (Data/IA en premier), puis par date
    # Priorité aux articles avec catégorie IA ou Data, puis par score, puis par date
    processed.sort(key=lambda x: (
        x['category'] not in ['ai', 'data'],  # IA et Data en premier
        -x['_relevance_score'],  # Score décroissant
        x['publishedAt']  # Date décroissante
    ))
    
    # Retirer les scores internes avant de retourner
    for article in processed:
        article.pop('_relevance_score', None)
        article.pop('_ai_score', None)
        article.pop('_data_score', None)
    
    # Filtrer pour avoir un bon équilibre : priorité aux articles vraiment IA et Data
    ai_articles = [a for a in processed if a['category'] == 'ai']
    data_articles = [a for a in processed if a['category'] == 'data']
    other_articles = [a for a in processed if a['category'] not in ['ai', 'data']]
    
    # Prendre jusqu'à 10 articles IA, 10 articles Data, et 5 autres
    final_articles = ai_articles[:10] + data_articles[:10] + other_articles[:5]
    
    return final_articles[:25]  # Maximum 25 articles

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
        
        # Récupérer les vidéos YouTube
        print("🎥 Récupération des vidéos YouTube...")
        youtube_videos = fetch_youtube_videos()
        print(f"📺 {len(youtube_videos)} vidéos YouTube récupérées")
        
        # Combiner articles et vidéos
        all_content = raw_articles + youtube_videos
        
        # Filtrer et traiter
        processed_articles = filter_and_process_articles(all_content)
        print(f"✨ {len(processed_articles)} contenus pertinents sélectionnés")
        
        # S'assurer qu'on a au moins quelques articles
        if len(processed_articles) == 0:
            print("⚠️  Aucun contenu trouvé, utilisation d'articles d'exemple")
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
