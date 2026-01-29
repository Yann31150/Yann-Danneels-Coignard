# Configuration de la Newsletter

## État actuel
Le système d'abonnement newsletter est actuellement en mode **simulation**. Les emails ne sont pas réellement stockés.

## Solution recommandée : Formspree (GRATUIT)

### Pourquoi Formspree ?
- ✅ Gratuit jusqu'à 50 soumissions/mois
- ✅ Aucun backend nécessaire
- ✅ Configuration en 5 minutes
- ✅ Reçoit les emails directement dans votre boîte mail
- ✅ Peut être exporté vers Mailchimp/autres services plus tard

### Étapes de configuration

1. **Créer un compte Formspree**
   - Allez sur https://formspree.io/
   - Cliquez sur "Sign Up" (gratuit)
   - Créez votre compte

2. **Créer un nouveau formulaire**
   - Une fois connecté, cliquez sur "New Form"
   - Donnez un nom : "Newsletter Actualités Tech"
   - Formspree vous donnera un ID (ex: `xjvqkzpn`)

3. **Configurer les notifications**
   - Dans les paramètres du formulaire, ajoutez votre email
   - Vous recevrez un email à chaque nouvel abonné

4. **Activer dans le code**
   - Ouvrez `docs/actualites-tech.html`
   - Trouvez la fonction `handleNewsletterSubmit`
   - Remplacez `YOUR_FORMSPREE_ID` par votre ID Formspree
   - Décommentez le code Formspree (supprimez les `/*` et `*/`)
   - Supprimez le `setTimeout` de simulation

5. **Tester**
   - Allez sur votre page Actualités Tech
   - Essayez de vous abonner avec votre email
   - Vérifiez que vous recevez l'email de notification

## Alternative : EmailJS

Si vous préférez EmailJS :

1. Créez un compte sur https://www.emailjs.com/
2. Configurez un service email (Gmail recommandé)
3. Créez un template email
4. Décommentez le code EmailJS dans `actualites-tech.html`
5. Remplacez les clés par vos vraies clés

## Gestion des abonnés

### Voir la liste des abonnés
- Connectez-vous à Formspree
- Allez dans votre formulaire
- Cliquez sur "Submissions" pour voir tous les emails

### Exporter les emails
- Dans Formspree, vous pouvez exporter en CSV
- Ou utiliser l'API Formspree pour récupérer les données

### Envoyer une newsletter
Pour envoyer une newsletter à tous vos abonnés :

1. **Option simple** : Utilisez Gmail avec la liste d'emails exportée
2. **Option professionnelle** : Migrez vers Mailchimp (gratuit jusqu'à 500 contacts)
   - Importez les emails depuis Formspree
   - Créez votre newsletter
   - Envoyez à tous les abonnés

## Migration future vers Mailchimp

Quand vous aurez besoin d'un système plus professionnel :

1. Créez un compte Mailchimp (gratuit jusqu'à 500 contacts)
2. Exportez vos emails depuis Formspree (CSV)
3. Importez-les dans Mailchimp
4. Utilisez l'API Mailchimp pour les nouveaux abonnements automatiques

## Fichiers concernés

- `docs/actualites-tech.html` - Formulaire d'abonnement
- `docs/newsletter-subscribers.json` - Fichier créé pour référence (non utilisé actuellement)

## Support

Si vous avez besoin d'aide pour configurer Formspree ou migrer vers un autre service, n'hésitez pas à demander !
