# Scripts d'actualités tech

Ce dossier contient les scripts pour automatiser la récupération des actualités tech quotidiennes.

## Configuration

### 1. Obtenir une clé API NewsAPI

1. Allez sur https://newsapi.org/
2. Créez un compte gratuit
3. Récupérez votre clé API (gratuite jusqu'à 100 requêtes/jour)

### 2. Configurer la clé API dans GitHub Secrets

1. Allez sur votre dépôt GitHub : `https://github.com/Yann31150/Yann-Danneels-Coignard`
2. Cliquez sur **Settings** → **Secrets and variables** → **Actions**
3. Cliquez sur **New repository secret**
4. Nom : `NEWS_API_KEY`
5. Valeur : Collez votre clé API NewsAPI
6. Cliquez sur **Add secret**

### 3. Tester le script localement

```bash
# Installer les dépendances
pip install requests

# Tester le script (sans clé API, il utilisera des données d'exemple)
python scripts/fetch_tech_news.py

# Avec la clé API
export NEWS_API_KEY="votre_cle_api"
python scripts/fetch_tech_news.py
```

## Fonctionnement

- Le workflow GitHub Actions s'exécute **tous les jours à 8h UTC** (9h heure française)
- Il récupère les articles tech des dernières 24h
- Filtre les articles pertinents avec des mots-clés
- Sauvegarde dans `docs/tech-news.json`
- Commit et push automatique vers le dépôt

## Déclencher manuellement

Vous pouvez déclencher le workflow manuellement :
1. Allez sur **Actions** dans votre dépôt GitHub
2. Sélectionnez le workflow **Update Tech News**
3. Cliquez sur **Run workflow**

## Personnalisation

Vous pouvez modifier les mots-clés dans `fetch_tech_news.py` pour cibler d'autres sujets.
