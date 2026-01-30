// Système de traduction multilingue EN/FR
const translations = {
    fr: {
        // Navigation
            nav: {
            accueil: "Accueil",
            apropos: "À propos",
            competences: "Compétences",
            outils: "Outils",
            passions: "Passions",
            projets: "Projets",
            cv: "Mon CV",
            databridge: "Databridge",
            actualites: "Actualités Tech",
            cybersecurite: "Cybersécurité",
            timeline: "Mon Parcours",
            contact: "Contact"
        },
        // Page d'accueil
        home: {
            title: "Yann Danneels-Coignard",
            subtitle: "Data Analyst",
            heroSubtitle: "Transformez vos données en insights stratégiques",
            viewCV: "Voir mon CV",
            downloadCV: "Télécharger le CV",
            availability: "Disponible pour CDD, CDI et alternance · Région toulousaine · Télétravail",
            recruitTitle: "Recruter un Data Analyst sérieux et motivé",
            whatIBring: "Ce que j'apporte",
            whatIBring1: "Analyse claire des données pour soutenir vos décisions.",
            whatIBring2: "Tableaux de bord efficaces sous Power BI.",
            whatIBring3: "SQL pour extraire, transformer et fiabiliser les KPI.",
            keySkills: "Compétences clés",
            contactMe: "Me contacter",
            viewProjects: "Voir mes projets",
            visits: "Visites",
            rights: "Tous droits réservés"
        },
        // Page projets
        projects: {
            title: "Mes Projets",
            project1Title: "Tableau de Bord pour une Entreprise de Maquettes",
            project1Objective: "Création d'un tableau de bord interactif pour la direction d'une entreprise spécialisée dans la vente de modèles et de maquettes, centré sur 4 axes clés : Ventes, Finances, Logistique et Ressources humaines.",
            project1Approach1: "Exploration des données & extraction des KPI en SQL",
            project1Approach1a: "Connexion à une base MySQL transactionnelle (OLTP)",
            project1Approach1b: "Rédaction de requêtes SQL avancées pour calculer les KPI",
            project1Approach1c: "Création de vues SQL pour faciliter l'import dans Power BI",
            project1Approach2: "Modélisation analytique (OLAP)",
            project1Approach2a: "Transformation vers un modèle en étoile",
            project1Approach2b: "Mise en place de tables de faits et dimensions",
            project1Approach2c: "Optimisation des performances",
            project1Approach3: "Construction du tableau de bord Power BI",
            project1Approach3a: "Intégration des vues SQL et modélisation",
            project1Approach3b: "Création de visuels pertinents",
            project1Approach3c: "Mise en place de filtres interactifs",
            project1Result: "Livraison d'un tableau de bord professionnel, interactif et actualisable permettant au directeur de piloter l'activité de son entreprise avec une vision claire et structurée.",
            download: "Télécharger le fichier Power BI",
            inProgress: "(en cours)",
            project2Title: "Système de recommandation de vins",
            project2Desc: "Projet de moteur de recommandation de vins pour un caviste local, avec analyse de données et machine learning.",
            project2Objective: "Proposer des recommandations personnalisées (accords mets-vins et préférences clients) pour augmenter la satisfaction et les ventes.",
            project2Approach1: "Nettoyage et structuration du catalogue (cépages, régions, prix, notes, styles).",
            project2Approach2: "Création de profils de goût à partir d'historiques d'achat et de retours clients.",
            project2Approach3: "Modèle hybride : similarité de contenu + popularité + contraintes métier.",
            project2Approach4: "Évaluation via tests A/B et métriques de pertinence (top-N).",
            project2Deliverables: "Livrables",
            project2Deliverable1: "Recommandations actionnables pour les vendeurs.",
            project2Deliverable2: "Tableau de bord des tendances et des paniers types.",
            project2Deliverable3: "Documentation d'usage et règles métier.",
            project3Title: "Ludrun : Votre Guide Intelligent pour Trouver Votre Prochain Jeu Vidéo",
            project3Desc: "Découvrez des jeux qui vous ressemblent, grâce à l'IA.",
            project3Vision: "Une plateforme de recommandations personnalisées, précises et surprenantes, basée sur le Machine Learning et l'IA avancée.",
            project3HowItWorks: "Comment ça marche ?",
            project3How1: "Vos goûts, notre matière première :",
            project3How1Desc: "analyse des jeux préférés, notes, heures de jeu et avis.",
            project3How2: "Une IA qui apprend en continu :",
            project3How2Desc: "modèles hybrides (collaboratif, contenu, contextuel) + données riches (genres, mécaniques, ambiances, tendances).",
            project3How3: "Des recommandations qui évoluent :",
            project3How3Desc: "suggestions selon l'humeur, sorties de zone de confort, styles ciblés.",
            project3How4: "Communauté de joueurs passionnés :",
            project3How4Desc: "listes partagées, comparaisons de goûts, recommandations validées.",
            project3Why: "Pourquoi choisir Ludrun ?",
            project3Why1: "Une IA qui comprend vos préférences, pas seulement vos achats.",
            project3Why2: "Découvertes intelligentes de pépites et classiques sous-estimés.",
            project3Why3: "Gain de temps : fini les recherches interminables.",
            project3Why4: "Gratuit, sans publicité intrusive.",
            project3OurVision: "Notre vision",
            project3OurVisionDesc: "Réinventer la découverte de jeux face à des recommandations souvent génériques, en combinant :",
            project3OurVision1: "Analyse comportementale (votre façon de jouer).",
            project3OurVision2: "Sémantique des jeux (mécaniques, ambiance, style narratif).",
            project3OurVision3: "Apprentissage continu (amélioration à chaque interaction)."
        },
        // Page compétences
        skills: {
            title: "DATA ANALYSE",
            dataAnalysis: "Analyse de données",
            dataVisualization: "Visualisation de données",
            databaseManagement: "Gestion de bases de données",
            statistics: "Statistiques descriptives et avancées",
            reporting: "Reporting et création de dashboards",
            problemSolving: "Résolution de problèmes et esprit critique",
            communication: "Communication et vulgarisation de résultats",
            bankingTitle: "COMPETENCES BANCAIRES",
            bankingTechnical: "🧠 Compétences techniques et professionnelles",
            bankingTechnical1: "Analyse financière (crédits entreprises, gestion des risques, financements syndiqués)",
            bankingTechnical2: "Analyse juridique de dossiers de successions",
            bankingTechnical3: "Montage et gestion de financements professionnels et immobiliers",
            bankingTechnical4: "Gestion de sûretés et décaissements",
            bankingTechnical5: "Traitement de dossiers de prêts immobiliers (y compris prêts réglementés)",
            bankingTechnical6: "Maîtrise du cycle bancaire (front, middle, back office)",
            bankingTechnical7: "Utilisation d'applicatifs bancaires : IPPI, CPM, Contact",
            bankingTechnical8: "Logiciels bureautiques : Word, Excel, Outlook",
            bankingTechnical9: "Validation AMF (Société Générale, 2016)",
            bankingSoft: "🤝 Compétences relationnelles et organisationnelles",
            bankingSoft1: "Gestion de portefeuille clients (jusqu'à 1200 comptes)",
            bankingSoft2: "Satisfaction client et sens du service",
            bankingSoft3: "Autonomie et sérieux",
            bankingSoft4: "Capacité d'adaptation",
            bankingSoft5: "Travail en équipe"
        },
        // Page outils
        tools: {
            title: "Outils & Technologies",
            dataEngineering: "Outils de Data Engineering",
            llm: "LLM & IA"
        },
        // Page contact
        contact: {
            title: "Contactez-moi",
            subtitle: "Disponible pour CDD, CDI et alternance",
            nameLabel: "Votre nom :",
            emailLabel: "Votre email :",
            messageLabel: "Votre message :",
            send: "Envoyer",
            linkedin: "LinkedIn",
            github: "GitHub",
            youtube: "YouTube"
        },
        // Page à propos
        about: {
            title: "À propos de moi",
            text1: "Après plus de 20 ans d'expérience dans le secteur bancaire, j'ai décidé de me réinventer professionnellement en me tournant vers un domaine qui me passionne : la data et la tech.",
            text2: "Actuellement en formation de Data Analyst à la Wild Code School de Toulouse, j'apprends à maîtriser les outils modernes d'analyse de données pour transformer l'information brute en leviers de décision pertinents.",
            text3: "Passionné par les technologies, l'analyse de données et leur impact stratégique, je suis à la recherche d'une alternance dans le domaine de la data.",
            text4: "Mon objectif : mettre mes compétences au service des entreprises pour comprendre les tendances, révéler des insights et améliorer la prise de décision."
        },
        // Page passions
        passions: {
            title: "Mes passions",
            intro: "Au-delà des chiffres et des tableaux de bord, je cultive des passions qui nourrissent autant ma rigueur que ma créativité.",
            shooting: "Le tir sportif",
            shootingDesc: "m'a appris la maîtrise de soi, la précision du geste et la concentration absolue. Chaque séance est un défi personnel où la technique rencontre la discipline, des qualités que j'aime retrouver dans mon métier de data analyst.",
            gaming: "Le gaming et les jeux de rôle",
            gamingDesc: "sont pour moi bien plus qu'un loisir : c'est un terrain d'exploration, de stratégie et d'imagination. J'adore plonger dans des univers complexes, résoudre des énigmes en équipe et repousser les limites de la créativité, que ce soit derrière un écran ou autour d'une table.",
            drone: "Enfin, en tant que",
            droneTitle: "télépilote de drone professionnel",
            droneDesc: "je combine technologie, vision et précision. Piloter un drone, c'est allier la rigueur du pilotage à l'art de la prise de vue, capturer des perspectives inédites et repousser les frontières du possible.",
            conclusion: "Ces passions, à la croisée du technique et du créatif, reflètent ma personnalité : sérieux, curieux, toujours prêt à relever de nouveaux défis et à partager des expériences uniques.",
            cta: "Envie d'en discuter ou de partager une partie ? Je suis toujours partant pour de nouvelles aventures !"
        },
        // Page cybersécurité
        cybersecurity: {
            title: "Cybersécurité 2026 : 10 Conseils Validés par l'IA"
        },
        // Page actualités tech
        techNews: {
            title: "Actualités Tech"
        },
        // Page CV
        cv: {
            title: "Mon CV",
            download: "Télécharger le CV en PDF"
        },
        // Page Databridge
        databridge: {
            title: "Databridge.ia",
            lead1: "Après une reconversion professionnelle dans la data, nous avons créé Databridge.ia avec une conviction simple : les données ne doivent pas être réservées aux géants du numérique ou aux experts.",
            lead2: "Que vous soyez TPE, PME, artisan ou indépendant, nous vous aidons à comprendre, exploiter et automatiser vos données pour prendre des décisions plus éclairées, sans jargon inutile ni usines à gaz.",
            contactUs: "Nous contacter",
            whyUs: "Pourquoi nous ?",
            whyUs1Title: "Des data analysts proches du terrain",
            whyUs1Desc: "Des solutions concrètes adaptées à vos réalités : Excel, Power BI, SQL, Python, automatisations simples.",
            whyUs2Title: "Une approche pédagogique",
            whyUs2Desc: "Nous expliquons clairement ce que vos données disent, sans vous noyer dans des équations.",
            whyUs3Title: "Des tarifs accessibles",
            whyUs3Desc: "Parce que la data ne doit pas être un luxe, nous proposons des forfaits adaptés aux petits budgets.",
            whyUs4Title: "De l'automatisation sans prise de tête",
            whyUs4Desc: "Gagnez du temps avec des scripts, tableaux de bord automatiques ou workflows qui libèrent vos équipes.",
            whatWeDo: "Ce que nous faisons pour vous",
            whatWeDo1Title: "Analyse exploratoire",
            whatWeDo1Desc: "Identifier tendances, anomalies et opportunités dans vos fichiers (ventes, RH, logistique).",
            whatWeDo2Title: "Tableaux de bord",
            whatWeDo2Desc: "Dashboards Power BI ou Excel pour suivre vos KPI en temps réel.",
            whatWeDo3Title: "Automatisation",
            whatWeDo3Desc: "Scripts Python pour automatiser vos tâches répétitives (rapports, exports, nettoyage de données).",
            whatWeDo4Title: "Formation",
            whatWeDo4Desc: "Vous former à l'analyse de données pour devenir autonome."
        },
        // Timeline
        timeline: {
            title: "Mon Parcours Professionnel",
            intro: "Découvrez mon parcours : de plus de 20 ans dans le secteur bancaire à ma reconversion passionnée vers la data analyse. Une transition guidée par la curiosité, l'apprentissage continu et la volonté de transformer les données en leviers de décision.",
            year1: "2003 - 2010",
            step1Title: "Début de Carrière dans le Secteur Bancaire",
            step1Subtitle: "Conseiller Clientèle & Analyste Financier",
            step1Desc: "Premiers pas dans le secteur bancaire avec une approche orientée client et analyse financière. Acquisition des fondamentaux : gestion de portefeuille, analyse de risques, montage de financements.",
            step1Skill1: "Gestion de portefeuille",
            step1Skill2: "Analyse financière",
            step1Skill3: "Relation client",
            year2: "2010 - 2024",
            step2Title: "Expertise et Spécialisation",
            step2Subtitle: "Analyste Senior & Gestion de Risques",
            step2Desc: "Développement d'une expertise approfondie en analyse financière, gestion des risques et financements complexes. Gestion de portefeuilles importants (jusqu'à 1200 comptes), analyse juridique de dossiers de successions jusqu'en 2024, validation AMF.",
            step2Skill1: "Gestion de risques",
            step2Skill2: "Financements syndiqués",
            step2Skill3: "Analyse juridique",
            step2Skill4: "Validation AMF",
            year3: "2020 - 2024",
            step3Title: "Prise de Conscience et Intérêt pour la Data",
            step3Subtitle: "Découverte de l'Analyse de Données",
            step3Desc: "Pendant cette période, réalisation que l'analyse de données et la data science représentent l'avenir. Intérêt croissant pour transformer l'information brute en insights actionnables. Début de l'apprentissage autodidacte en Python, SQL et visualisation de données, tout en continuant l'analyse juridique de successions jusqu'en 2024.",
            step3Skill1: "Python",
            step3Skill2: "SQL",
            step3Skill3: "Visualisation",
            step3Skill4: "Autoformation",
            year4: "2024",
            step4Title: "Décision de Reconversion",
            step4Subtitle: "Transition vers la Data Analyse",
            step4Desc: "Après plus de 20 ans dans le secteur bancaire, décision de se réinventer professionnellement. Choix de se tourner vers un domaine en pleine expansion qui combine analyse, technologie et impact stratégique : la data analyse.",
            step4Skill1: "Reconversion",
            step4Skill2: "Nouveau départ",
            step4Skill3: "Motivation",
            year5: "2024 - 2025",
            step5Title: "Formation Data Analyst",
            step5Subtitle: "Wild Code School Toulouse",
            step5Desc: "Intégration de la Wild Code School de Toulouse pour une formation intensive en Data Analyst. Apprentissage des outils modernes : SQL avancé, Power BI, Python (Pandas, NumPy, Matplotlib), statistiques, machine learning, data storytelling.",
            step5Skill1: "Power BI",
            step5Skill2: "Python",
            step5Skill3: "SQL",
            step5Skill4: "Machine Learning",
            step5Skill5: "Data Storytelling",
            year6: "2025",
            step6Title: "Projets Concrets et Mise en Pratique",
            step6Subtitle: "Réalisation de Projets Data",
            step6Desc: "Développement de projets concrets : tableau de bord Power BI pour une entreprise de maquettes, système de recommandation de vins avec machine learning, projet Ludrun (recommandation de jeux vidéo avec IA). Application pratique des compétences acquises. À partir de fin 2025, début de projets freelance dans le cadre de Databridge.ia.",
            step6Skill1: "Dashboards Power BI",
            step6Skill2: "Machine Learning",
            step6Skill3: "Recommandation IA",
            step6Skill4: "Projets réels",
            step6Skill5: "Freelance",
            step6Skill6: "Databridge.ia",
            year7: "2026",
            step7Title: "Aujourd'hui : Disponible en tant que Data Analyst",
            step7Subtitle: "Alternance, CDD ou CDI - Data Analyst, Data Scientist ou Data Engineer",
            step7Desc: "Recherche active d'une opportunité en tant que Data Analyst (CDD/CDI), ou alternance en tant que Data Analyst, Data Scientist ou Data Engineer pour continuer à apprendre tout en apportant ma valeur ajoutée. Projets freelance en cours dans le cadre de Databridge.ia. Disponible dès maintenant, région toulousaine ou télétravail. Prêt à transformer vos données en insights stratégiques.",
            step7Skill1: "Data Analyst",
            step7Skill2: "Data Scientist",
            step7Skill3: "Data Engineer",
            step7Skill4: "Alternance",
            step7Skill5: "CDD/CDI",
            step7Skill6: "Toulouse",
            step7Skill7: "Télétravail",
            step7Skill8: "Freelance",
            step7Skill9: "Databridge.ia"
        }
    },
    en: {
        // Navigation
        nav: {
            accueil: "Home",
            apropos: "About",
            competences: "Skills",
            outils: "Tools",
            passions: "Passions",
            projets: "Projects",
            cv: "My CV",
            databridge: "Databridge",
            actualites: "Tech News",
            cybersecurite: "Cybersecurity",
            timeline: "My Journey",
            contact: "Contact"
        },
        // Page d'accueil
        home: {
            title: "Yann Danneels-Coignard",
            subtitle: "Data Analyst",
            heroSubtitle: "Transform your data into strategic insights",
            viewCV: "View my CV",
            downloadCV: "Download CV",
            availability: "Available for fixed-term contract, permanent contract and apprenticeship · Toulouse region · Remote work",
            recruitTitle: "Hire a serious and motivated Data Analyst",
            whatIBring: "What I bring",
            whatIBring1: "Clear data analysis to support your decisions.",
            whatIBring2: "Effective dashboards with Power BI.",
            whatIBring3: "SQL to extract, transform and ensure KPI reliability.",
            keySkills: "Key Skills",
            contactMe: "Contact me",
            viewProjects: "View my projects",
            visits: "Visits",
            rights: "All rights reserved"
        },
        // Page projets
        projects: {
            title: "My Projects",
            project1Title: "Dashboard for a Model Company",
            project1Objective: "Creation of an interactive dashboard for the management of a company specializing in the sale of models and scale models, focused on 4 key areas: Sales, Finance, Logistics and Human Resources.",
            project1Approach1: "Data exploration & KPI extraction in SQL",
            project1Approach1a: "Connection to a transactional MySQL database (OLTP)",
            project1Approach1b: "Writing advanced SQL queries to calculate KPIs",
            project1Approach1c: "Creating SQL views to facilitate import into Power BI",
            project1Approach2: "Analytical modeling (OLAP)",
            project1Approach2a: "Transformation to a star model",
            project1Approach2b: "Setting up fact and dimension tables",
            project1Approach2c: "Performance optimization",
            project1Approach3: "Building the Power BI dashboard",
            project1Approach3a: "Integration of SQL views and modeling",
            project1Approach3b: "Creating relevant visuals",
            project1Approach3c: "Setting up interactive filters",
            project1Result: "Delivery of a professional, interactive and updatable dashboard enabling the director to manage his company's activity with a clear and structured vision.",
            download: "Download Power BI file",
            inProgress: "(in progress)",
            project2Title: "Wine recommendation system",
            project2Desc: "Wine recommendation engine project for a local wine merchant, with data analysis and machine learning.",
            project2Objective: "Provide personalized recommendations (food-wine pairings and customer preferences) to increase satisfaction and sales.",
            project2Approach1: "Cleaning and structuring the catalog (grape varieties, regions, prices, ratings, styles).",
            project2Approach2: "Creating taste profiles from purchase history and customer feedback.",
            project2Approach3: "Hybrid model: content similarity + popularity + business constraints.",
            project2Approach4: "Evaluation via A/B testing and relevance metrics (top-N).",
            project2Deliverables: "Deliverables",
            project2Deliverable1: "Actionable recommendations for salespeople.",
            project2Deliverable2: "Dashboard of trends and typical baskets.",
            project2Deliverable3: "Usage documentation and business rules.",
            project3Title: "Ludrun: Your Intelligent Guide to Finding Your Next Video Game",
            project3Desc: "Discover games that match your style, thanks to AI.",
            project3Vision: "A platform for personalized, precise and surprising recommendations, based on Machine Learning and advanced AI.",
            project3HowItWorks: "How it works?",
            project3How1: "Your tastes, our raw material:",
            project3How1Desc: "analysis of favorite games, ratings, playtime and reviews.",
            project3How2: "An AI that learns continuously:",
            project3How2Desc: "hybrid models (collaborative, content, contextual) + rich data (genres, mechanics, atmospheres, trends).",
            project3How3: "Recommendations that evolve:",
            project3How3Desc: "suggestions based on mood, stepping out of comfort zone, targeted styles.",
            project3How4: "Community of passionate players:",
            project3How4Desc: "shared lists, taste comparisons, validated recommendations.",
            project3Why: "Why choose Ludrun?",
            project3Why1: "An AI that understands your preferences, not just your purchases.",
            project3Why2: "Intelligent discovery of gems and underestimated classics.",
            project3Why3: "Time savings: no more endless searches.",
            project3Why4: "Free, without intrusive advertising.",
            project3OurVision: "Our vision",
            project3OurVisionDesc: "Reinvent game discovery in the face of often generic recommendations, by combining:",
            project3OurVision1: "Behavioral analysis (how you play).",
            project3OurVision2: "Game semantics (mechanics, atmosphere, narrative style).",
            project3OurVision3: "Continuous learning (improvement with each interaction)."
        },
        // Page compétences
        skills: {
            title: "DATA ANALYSIS",
            dataAnalysis: "Data analysis",
            dataVisualization: "Data visualization",
            databaseManagement: "Database management",
            statistics: "Descriptive and advanced statistics",
            reporting: "Reporting and dashboard creation",
            problemSolving: "Problem solving and critical thinking",
            communication: "Communication and results popularization",
            bankingTitle: "BANKING SKILLS",
            bankingTechnical: "🧠 Technical and professional skills",
            bankingTechnical1: "Financial analysis (corporate loans, risk management, syndicated financing)",
            bankingTechnical2: "Legal analysis of inheritance files",
            bankingTechnical3: "Structuring and management of professional and real estate financing",
            bankingTechnical4: "Collateral and disbursement management",
            bankingTechnical5: "Processing of mortgage loan files (including regulated loans)",
            bankingTechnical6: "Mastery of the banking cycle (front, middle, back office)",
            bankingTechnical7: "Use of banking applications: IPPI, CPM, Contact",
            bankingTechnical8: "Office software: Word, Excel, Outlook",
            bankingTechnical9: "AMF validation (Société Générale, 2016)",
            bankingSoft: "🤝 Relational and organizational skills",
            bankingSoft1: "Client portfolio management (up to 1200 accounts)",
            bankingSoft2: "Customer satisfaction and service orientation",
            bankingSoft3: "Autonomy and seriousness",
            bankingSoft4: "Adaptability",
            bankingSoft5: "Teamwork"
        },
        // Page outils
        tools: {
            title: "Tools & Technologies",
            dataEngineering: "Data Engineering Tools",
            llm: "LLM & AI"
        },
        // Page contact
        contact: {
            title: "Contact me",
            subtitle: "Available for fixed-term contract, permanent contract and apprenticeship",
            nameLabel: "Your name:",
            emailLabel: "Your email:",
            messageLabel: "Your message:",
            send: "Send",
            linkedin: "LinkedIn",
            github: "GitHub",
            youtube: "YouTube"
        },
        // Page à propos
        about: {
            title: "About me",
            text1: "After more than 20 years of experience in the banking sector, I decided to professionally reinvent myself by turning to a field that I am passionate about: data and tech.",
            text2: "Currently training as a Data Analyst at Wild Code School in Toulouse, I am learning to master modern data analysis tools to transform raw information into relevant decision-making levers.",
            text3: "Passionate about technologies, data analysis and their strategic impact, I am looking for an apprenticeship in the data field.",
            text4: "My goal: put my skills at the service of companies to understand trends, reveal insights and improve decision-making."
        },
        // Page passions
        passions: {
            title: "My Passions",
            intro: "Beyond numbers and dashboards, I cultivate passions that nourish both my rigor and my creativity.",
            shooting: "Sport shooting",
            shootingDesc: "taught me self-control, precision of gesture and absolute concentration. Each session is a personal challenge where technique meets discipline, qualities I like to find in my work as a data analyst.",
            gaming: "Gaming and role-playing games",
            gamingDesc: "are much more than a hobby for me: it's a field of exploration, strategy and imagination. I love diving into complex universes, solving puzzles as a team and pushing the limits of creativity, whether behind a screen or around a table.",
            drone: "Finally, as a",
            droneTitle: "professional drone pilot",
            droneDesc: "I combine technology, vision and precision. Flying a drone means combining the rigor of piloting with the art of photography, capturing unique perspectives and pushing the boundaries of what's possible.",
            conclusion: "These passions, at the crossroads of technical and creative, reflect my personality: serious, curious, always ready to take on new challenges and share unique experiences.",
            cta: "Want to discuss or share a game? I'm always up for new adventures!"
        },
        // Page cybersécurité
        cybersecurity: {
            title: "Cybersecurity 2026: 10 AI-Validated Tips"
        },
        // Page actualités tech
        techNews: {
            title: "Tech News"
        },
        // Page CV
        cv: {
            title: "My CV",
            download: "Download CV in PDF"
        },
        // Page Databridge
        databridge: {
            title: "Databridge.ia",
            lead1: "After a professional retraining in data, we created Databridge.ia with a simple conviction: data should not be reserved for digital giants or experts.",
            lead2: "Whether you are a small business, SME, craftsman or freelancer, we help you understand, exploit and automate your data to make more informed decisions, without unnecessary jargon or overcomplicated solutions.",
            contactUs: "Contact us",
            whyUs: "Why us?",
            whyUs1Title: "Data analysts close to the field",
            whyUs1Desc: "Concrete solutions adapted to your realities: Excel, Power BI, SQL, Python, simple automations.",
            whyUs2Title: "A pedagogical approach",
            whyUs2Desc: "We clearly explain what your data says, without drowning you in equations.",
            whyUs3Title: "Affordable rates",
            whyUs3Desc: "Because data should not be a luxury, we offer packages adapted to small budgets.",
            whyUs4Title: "Automation without hassle",
            whyUs4Desc: "Save time with scripts, automatic dashboards or workflows that free up your teams.",
            whatWeDo: "What we do for you",
            whatWeDo1Title: "Exploratory analysis",
            whatWeDo1Desc: "Identify trends, anomalies and opportunities in your files (sales, HR, logistics).",
            whatWeDo2Title: "Dashboards",
            whatWeDo2Desc: "Power BI or Excel dashboards to track your KPIs in real time.",
            whatWeDo3Title: "Automation",
            whatWeDo3Desc: "Python scripts to automate your repetitive tasks (reports, exports, data cleaning).",
            whatWeDo4Title: "Training",
            whatWeDo4Desc: "Train you in data analysis to become autonomous."
        },
        // Timeline
        timeline: {
            title: "My Professional Journey",
            intro: "Discover my journey: from over 20 years in the banking sector to my passionate transition to data analysis. A transition guided by curiosity, continuous learning and the desire to transform data into decision-making levers.",
            year1: "2003 - 2010",
            step1Title: "Start of Career in Banking",
            step1Subtitle: "Client Advisor & Financial Analyst",
            step1Desc: "First steps in the banking sector with a client-oriented approach and financial analysis. Acquisition of fundamentals: portfolio management, risk analysis, financing structuring.",
            step1Skill1: "Portfolio management",
            step1Skill2: "Financial analysis",
            step1Skill3: "Client relations",
            year2: "2010 - 2024",
            step2Title: "Expertise and Specialization",
            step2Subtitle: "Senior Analyst & Risk Management",
            step2Desc: "Development of in-depth expertise in financial analysis, risk management and complex financing. Management of large portfolios (up to 1200 accounts), legal analysis of inheritance files until 2024, AMF validation.",
            step2Skill1: "Risk management",
            step2Skill2: "Syndicated financing",
            step2Skill3: "Legal analysis",
            step2Skill4: "AMF validation",
            year3: "2020 - 2024",
            step3Title: "Awareness and Interest in Data",
            step3Subtitle: "Discovery of Data Analysis",
            step3Desc: "During this period, realization that data analysis and data science represent the future. Growing interest in transforming raw information into actionable insights. Beginning of self-taught learning in Python, SQL and data visualization, while continuing legal analysis of inheritances until 2024.",
            step3Skill1: "Python",
            step3Skill2: "SQL",
            step3Skill3: "Visualization",
            step3Skill4: "Self-training",
            year4: "2024",
            step4Title: "Career Change Decision",
            step4Subtitle: "Transition to Data Analysis",
            step4Desc: "After more than 20 years in the banking sector, decision to professionally reinvent oneself. Choice to turn to a growing field that combines analysis, technology and strategic impact: data analysis.",
            step4Skill1: "Career change",
            step4Skill2: "Fresh start",
            step4Skill3: "Motivation",
            year5: "2024 - 2025",
            step5Title: "Data Analyst Training",
            step5Subtitle: "Wild Code School Toulouse",
            step5Desc: "Integration of Wild Code School Toulouse for intensive Data Analyst training. Learning modern tools: advanced SQL, Power BI, Python (Pandas, NumPy, Matplotlib), statistics, machine learning, data storytelling.",
            step5Skill1: "Power BI",
            step5Skill2: "Python",
            step5Skill3: "SQL",
            step5Skill4: "Machine Learning",
            step5Skill5: "Data Storytelling",
            year6: "2025",
            step6Title: "Concrete Projects and Practice",
            step6Subtitle: "Data Project Implementation",
            step6Desc: "Development of concrete projects: Power BI dashboard for a model company, wine recommendation system with machine learning, Ludrun project (video game recommendation with AI). Practical application of acquired skills. From late 2025, start of freelance projects within Databridge.ia.",
            step6Skill1: "Power BI Dashboards",
            step6Skill2: "Machine Learning",
            step6Skill3: "AI Recommendation",
            step6Skill4: "Real projects",
            step6Skill5: "Freelance",
            step6Skill6: "Databridge.ia",
            year7: "2026",
            step7Title: "Today: Available as a Data Analyst",
            step7Subtitle: "Apprenticeship, Fixed-term or Permanent Contract - Data Analyst, Data Scientist or Data Engineer",
            step7Desc: "Active search for an opportunity as a Data Analyst (fixed-term or permanent contract), or apprenticeship as a Data Analyst, Data Scientist or Data Engineer to continue learning while bringing my added value. Ongoing freelance projects within Databridge.ia. Available now, Toulouse region or remote work. Ready to transform your data into strategic insights.",
            step7Skill1: "Data Analyst",
            step7Skill2: "Data Scientist",
            step7Skill3: "Data Engineer",
            step7Skill4: "Apprenticeship",
            step7Skill5: "Fixed-term/Permanent",
            step7Skill6: "Toulouse",
            step7Skill7: "Remote work",
            step7Skill8: "Freelance",
            step7Skill9: "Databridge.ia"
        }
    }
};

// Fonction pour obtenir la langue actuelle
function getCurrentLanguage() {
    return localStorage.getItem('language') || 'fr';
}

// Fonction pour définir la langue
function setLanguage(lang) {
    localStorage.setItem('language', lang);
    applyTranslations(lang);
    updateLanguageSelector(lang);
}

// Fonction pour appliquer les traductions
function applyTranslations(lang) {
    const t = translations[lang];
    if (!t) return;

    // Traduire les éléments avec data-translate
    document.querySelectorAll('[data-translate]').forEach(element => {
        const key = element.getAttribute('data-translate');
        const keys = key.split('.');
        let value = t;
        
        for (const k of keys) {
            value = value?.[k];
        }
        
        if (value) {
            if (element.tagName === 'INPUT' && element.type === 'submit') {
                element.value = value;
            } else if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
                element.placeholder = value;
            } else {
                element.textContent = value;
            }
        }
    });

    // Traduire les attributs alt et title
    document.querySelectorAll('[data-translate-alt]').forEach(element => {
        const key = element.getAttribute('data-translate-alt');
        const keys = key.split('.');
        let value = t;
        
        for (const k of keys) {
            value = value?.[k];
        }
        
        if (value) {
            element.alt = value;
            element.title = value;
        }
    });

    // Mettre à jour la langue du document
    document.documentElement.lang = lang;
}

// Fonction pour mettre à jour le sélecteur de langue
function updateLanguageSelector(currentLang) {
    const langButtons = document.querySelectorAll('.lang-btn');
    langButtons.forEach(btn => {
        if (btn.dataset.lang === currentLang) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });
}

// Initialiser la langue au chargement
document.addEventListener('DOMContentLoaded', function() {
    const currentLang = getCurrentLanguage();
    applyTranslations(currentLang);
    updateLanguageSelector(currentLang);
});
