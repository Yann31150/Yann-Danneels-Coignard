# Comment stocker les adresses email des abonnés

## Solution recommandée : Formspree (GRATUIT et SIMPLE)

Formspree est un service gratuit qui **stocke automatiquement** tous les emails dans votre compte. C'est comme une boîte mail dédiée pour vos abonnés.

### Pourquoi Formspree ?
- ✅ **Gratuit** jusqu'à 50 abonnés/mois
- ✅ **Stockage automatique** - Tous les emails sont sauvegardés
- ✅ **Aucun backend** nécessaire - Fonctionne directement depuis votre site
- ✅ **Export CSV** - Vous pouvez télécharger tous les emails en un clic
- ✅ **Configuration en 2 minutes**

### Étapes de configuration (2 minutes)

1. **Créer un compte Formspree**
   - Allez sur https://formspree.io/
   - Cliquez sur "Sign Up" (gratuit)
   - Créez votre compte avec votre email

2. **Créer un formulaire**
   - Une fois connecté, cliquez sur **"New Form"**
   - Donnez un nom : "Newsletter Actualités Tech"
   - Formspree vous donnera un **ID** (ex: `xjvqkzpn`)
   - **Copiez cet ID**

3. **Activer dans votre code**
   - Ouvrez `docs/actualites-tech.html`
   - Cherchez `YOUR_FORMSPREE_ID` dans le code
   - Remplacez-le par votre ID (ex: `xjvqkzpn`)
   - Décommentez le code (supprimez les `/*` et `*/` autour du code Formspree)
   - Supprimez le `setTimeout` de simulation

4. **Tester**
   - Allez sur votre page Actualités Tech
   - Essayez de vous abonner
   - Vérifiez dans Formspree que l'email apparaît

### Voir vos abonnés

1. Connectez-vous à Formspree
2. Cliquez sur votre formulaire "Newsletter Actualités Tech"
3. Cliquez sur **"Submissions"**
4. Vous verrez tous les emails stockés avec la date d'abonnement

### Exporter vos emails

1. Dans Formspree, allez dans **"Submissions"**
2. Cliquez sur **"Export"** → **"CSV"**
3. Téléchargez le fichier CSV avec tous les emails

### Exemple de code à activer

Une fois que vous avez votre ID Formspree, remplacez ceci :
```javascript
fetch('https://formspree.io/f/YOUR_FORMSPREE_ID', {
```

Par ceci (avec votre vrai ID) :
```javascript
fetch('https://formspree.io/f/xjvqkzpn', {
```

## Alternative : Stockage manuel

Si vous préférez ne pas utiliser de service externe, vous pouvez :

1. **Vérifier manuellement** les emails dans Formspree
2. **Copier-coller** les emails dans un fichier Excel/Google Sheets
3. **Utiliser plus tard** pour envoyer des newsletters

## Questions fréquentes

**Q : Les emails sont-ils sécurisés ?**
R : Oui, Formspree est un service reconnu utilisé par des milliers de sites. Vos données sont privées.

**Q : Puis-je exporter mes emails plus tard ?**
R : Oui, vous pouvez exporter en CSV à tout moment.

**Q : Que se passe-t-il si j'ai plus de 50 abonnés ?**
R : Le plan gratuit permet 50 soumissions/mois. Au-delà, vous pouvez passer au plan payant ou exporter vos emails et utiliser un autre service.

**Q : Puis-je migrer vers Mailchimp plus tard ?**
R : Oui, vous pouvez exporter vos emails depuis Formspree et les importer dans Mailchimp.

## Besoin d'aide ?

Si vous avez besoin d'aide pour configurer Formspree, dites-moi et je peux vous guider étape par étape !
