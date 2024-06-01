# zoo-arcadia-app

Arcadia Zoo Web Application
Introduction

Arcadia Zoo Web Application est une application web conçue pour permettre aux visiteurs de visualiser les animaux, leurs états de santé, et les services offerts par le zoo. L'application comprend des espaces spécifiques pour les administrateurs, les employés et les vétérinaires pour gérer différentes fonctionnalités.
Table des matières

    1)Technologies utilisées
    Pré-requis
    Installation
    Configuration
    Lancer l'application
    Fonctionnalités
    Structure du projet
    Contribuer
    Licence
    2) user stories
    

Technologies utilisées

    Front-end: HTML5, CSS (Bootstrap), JavaScript
    Back-end: PHP avec PDO
    Base de données: MySQL pour la base de données relationnelle, MongoDB pour la base de données NoSQL
    Déploiement: Heroku

Pré-requis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

    Git
    PHP
    Composer
    MySQL
    MongoDB
    Node.js et npm (pour gérer les dépendances front-end)

Installation

    Cloner le dépôt GitHub :

    sh

git clone https://github.com/username/arcadia-zoo-webapp.git
cd arcadia-zoo-webapp

Installer les dépendances back-end :

sh

composer install

Installer les dépendances front-end :

sh

    npm install

Configuration

    Configurer la base de données MySQL :
        Créez une base de données MySQL.
        Importez le fichier database/schema.sql pour créer les tables nécessaires.
        Importez le fichier database/data.sql pour insérer les données initiales.

    Configurer la base de données MongoDB :
        Démarrez MongoDB.
        La collection pour les statistiques de consultation des animaux sera créée automatiquement lors de la première utilisation.

    Configurer le fichier .env :
        Créez un fichier .env à la racine du projet.
        Ajoutez les configurations suivantes :

    env

    DB_HOST=localhost
    DB_NAME=arcadia_zoo
    DB_USER=root
    DB_PASS=password

    MONGO_URI=mongodb://localhost:27017
    MONGO_DB=arcadia_zoo

    MAIL_HOST=smtp.example.com
    MAIL_PORT=587
    MAIL_USER=no-reply@example.com
    MAIL_PASS=password

Lancer l'application

    Démarrer le serveur PHP :

    sh

    php -S localhost:8000 -t public

    Accéder à l'application :
        Ouvrez votre navigateur et allez à l'adresse http://localhost:8000.

Fonctionnalités

    Visiteurs :
        Accueil : Présentation du zoo, des habitats, des services et des avis des visiteurs.
        Consultation des habitats et des animaux.
        Soumission d'avis.

    Administrateurs :
        Gestion des comptes employés et vétérinaires.
        Gestion des services, horaires, habitats et animaux.
        Visualisation des comptes rendus vétérinaires et des statistiques de consultation.

    Employés :
        Validation des avis des visiteurs.
        Gestion de l'alimentation des animaux.

    Vétérinaires :
        Remplissage des comptes rendus de santé des animaux.
        Consultation de l'historique alimentaire des animaux.

Structure du projet

kotlin

arcadia-zoo-webapp/
├── database/
│   ├── schema.sql
│   ├── data.sql
├── public/
│   ├── index.php
│   ├── css/
│   ├── js/
├── src/
│   ├── controllers/
│   ├── models/
│   ├── views/
├── .env
├── composer.json
├── package.json
├── README.md

Contribuer

Les contributions sont les bienvenues ! Veuillez suivre les étapes suivantes pour contribuer :

    Fork le projet.
    Créez une branche pour votre fonctionnalité (git checkout -b feature/ma-fonctionnalité).
    Commitez vos modifications (git commit -m 'Ajout de ma fonctionnalité').
    Pushez votre branche (git push origin feature/ma-fonctionnalité).
    Ouvrez une Pull Request.
User Stories (US) en Détail

    US 1 : Page d’accueil
        Description : La page d'accueil doit présenter le zoo avec quelques images, les différents habitats, services et animaux, ainsi que les avis des visiteurs.
        Critères d'acceptation :
            Présentation du zoo avec au moins trois images.
            Liste des habitats (savane, jungle, marais).
            Liste des services offerts par le zoo.
            Avis des visiteurs affichés sur la page.

    US 2 : Menu de l’application
        Description : Le menu de l'application permet de naviguer facilement entre les différentes sections.
        Critères d'acceptation :
            Lien vers la page d'accueil.
            Lien vers la page des services.
            Lien vers la page des habitats.
            Lien de connexion pour les vétérinaires, employés et administrateurs.
            Lien vers la page de contact.

    US 3 : Vue globale de tous les services
        Description : Une page récapitulative affichant tous les services proposés par le zoo.
        Critères d'acceptation :
            Affichage du nom et de la description de chaque service.
            Possibilité de configurer les services depuis l'espace administrateur.

    US 4 : Vue globale des habitats
        Description : Une page présentant tous les habitats avec les animaux associés.
        Critères d'acceptation :
            Affichage de tous les habitats avec image et nom.
            Détail des habitats avec description et liste des animaux.
            Affichage de l'état de santé des animaux et détails des visites vétérinaires.

    US 5 : Avis
        Description : Les visiteurs peuvent laisser des commentaires qui seront validés par les employés.
        Critères d'acceptation :
            Formulaire pour laisser un avis avec pseudo et texte.
            Système de validation par un employé avant publication sur la page d'accueil.

    US 6 : Espace Administrateur
        Description : Les administrateurs peuvent gérer les comptes, services, horaires, habitats, et animaux.
        Critères d'acceptation :
            Création, mise à jour et suppression des comptes employés et vétérinaires.
            Gestion des services, horaires, habitats et animaux.
            Visualisation et filtrage des comptes rendus vétérinaires.
            Dashboard avec statistiques de consultation des animaux.

    US 7 : Espace Employé
        Description : Les employés peuvent valider les avis des visiteurs et gérer la nourriture des animaux.
        Critères d'acceptation :
            Validation et invalidation des avis.
            Gestion de l'alimentation quotidienne des animaux avec date, heure, nourriture et quantité.

    US 8 : Espace Vétérinaire
        Description : Les vétérinaires remplissent les comptes rendus de santé des animaux et peuvent commenter sur les habitats.
        Critères d'acceptation :
            Remplissage des comptes rendus par animal.
            Ajout de commentaires sur l'état des habitats.
            Visualisation de l'historique alimentaire des animaux.

    US 9 : Connexion
        Description : Les administrateurs, vétérinaires et employés peuvent se connecter avec un username (email) et mot de passe.
        Critères d'acceptation :
            Formulaire de connexion sécurisé.
            Accès restreint aux utilisateurs autorisés (administrateurs, vétérinaires, employés).

    US 10 : Contact
        Description : Les visiteurs peuvent contacter le zoo via un formulaire de contact.
        Critères d'acceptation :
            Formulaire de contact avec titre, description et email.
            Envoi de la demande par email au zoo.
            Réponse possible par email depuis l'espace employé.

    US 11 : Statistiques sur la consultation des habitats
        Description : Suivi des consultations des animaux par les visiteurs.
        Critères d'acceptation :
            Incrémentation du compteur de consultation à chaque clic sur un animal.
            Stockage des données de consultation dans une base de données NoSQL.
            Visualisation des statistiques dans le dashboard administrateur.

Spécifications Techniques et Sécurité

    Sécurité
        Utilisation de connexions HTTPS.
        Hashage des mots de passe avant stockage.
        Protection contre les attaques CSRF et XSS.
        Validation des entrées utilisateurs pour éviter les injections SQL.

    Base de Données
        Relationnelle (MySQL) :
            Tables pour les utilisateurs, animaux, habitats, services, avis, rapports vétérinaires.
        NoSQL (MongoDB) :
            Collection pour les statistiques de consultation des animaux.

    Front-End
        Utilisation de Bootstrap pour le design responsive.
        JavaScript pour l'interactivité.
        HTML5 et CSS pour la structure et le style.

    Back-End
        Utilisation de PHP avec PDO pour la gestion des interactions avec la base de données.
        API RESTful pour la communication entre le front-end et le back-end.

    Déploiement
        Déploiement sur Heroku avec configuration appropriée pour les bases de données et les variables d'environnement.

Critères d'Acceptation pour Chaque User Story

    US 1 : Page d’accueil
         présence de la présentation du zoo, des images, des habitats, des services, et des avis des visiteurs.
        Testez la réactivité de la page sur différentes tailles d'écran.

    US 2 : Menu de l’application
        les liens du menu fonctionnent et redirigent correctement.
        accessibilité du menu sur différents appareils.

    US 3 : Vue globale de tous les services
         les services sont affichés avec leur nom et description.
         configuration des services depuis l'espace administrateur.

    US 4 : Vue globale des habitats
         les habitats sont affichés avec image et nom.
         les détails des habitats et des animaux s'affichent correctement au clic.
         l'affichage des états de santé des animaux.

    US 5 : Avis
         les visiteurs peuvent soumettre des avis et que les employés peuvent les valider/invalider.
         l'affichage des avis validés sur la page d'accueil.

    US 6 : Espace Administrateur
         l'administrateur peut créer, mettre à jour, et supprimer les comptes, services, horaires, habitats, et animaux.
        les fonctionnalités de visualisation et de filtrage des comptes rendus vétérinaires.
        Vérification le dashboard des statistiques de consultation des animaux.

    US 7 : Espace Employé
        Vérification que les employés peuvent valider/invalider les avis et gérer l'alimentation des animaux.
        Testez la saisie de l'alimentation quotidienne avec date, heure, nourriture et quantité.

    US 8 : Espace Vétérinaire
         les vétérinaires peuvent remplir les comptes rendus et commenter sur les habitats.
          visualisation de l'historique alimentaire des animaux.

    US 9 : Connexion
        Teste du  formulaire de connexion pour les administrateurs, vétérinaires, et employés.
         les utilisateurs non autorisés ne peuvent pas se connecter.

    US 10 : Contact
        le formulaire de contact fonctionne et envoie les demandes par email.
        Teste de la réponse aux demandes par email depuis l'espace employé.

    US 11 : Statistiques sur la consultation des habitats
        Assurez-vous que le compteur de consultation s'incrémente à chaque clic sur un animal.
        Vérification que les données de consultation sont correctement stockées dans la base de données NoSQL.
        Test de l'affichage des statistiques dans le dashboard administrateur.

