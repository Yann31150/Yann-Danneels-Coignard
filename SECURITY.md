# Sécurité - Gestion des clés API

## ⚠️ IMPORTANT - Ne jamais exposer les clés API

**NE JAMAIS** :
- ❌ Commiter des clés API dans le code
- ❌ Mettre des clés API dans des fichiers de configuration versionnés
- ❌ Partager des clés API publiquement
- ❌ Mettre des clés API dans des commentaires de code

**TOUJOURS** :
- ✅ Utiliser GitHub Secrets pour stocker les clés API
- ✅ Utiliser des variables d'environnement (`os.getenv()`)
- ✅ Vérifier que `.gitignore` exclut les fichiers sensibles
- ✅ Révoquer immédiatement toute clé API exposée

## Configuration des secrets GitHub

Les clés API doivent être configurées dans :
**Settings** → **Secrets and variables** → **Actions**

- `NEWS_API_KEY` : Clé API NewsAPI
- `YOUTUBE_API_KEY` : Clé API YouTube Data API v3

## En cas d'exposition d'une clé API

1. **Révoquer immédiatement** la clé dans la console du fournisseur
2. **Créer une nouvelle clé** si nécessaire
3. **Mettre à jour** le secret GitHub avec la nouvelle clé
4. **Vérifier l'historique Git** pour supprimer les commits contenant la clé exposée
