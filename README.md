# Projet de Scraping d'Images Google avec Selenium
Description

Ce script Python utilise Selenium avec undetected_chromedriver pour automatiser le scraping d'images depuis Google Images. Il prend en charge différentes catégories de mots-clés, tels que "nature", "maison", "manoir", etc., avec des angles de vue spécifiés comme "été", "hiver", "automne", "printemps", "jour" et "nuit".
Prérequis

    Python 3.x
    undetected_chromedriver
    Selenium
    winsound (pour la notification sonore, compatible uniquement avec les systèmes Windows)

Installation

    Installez les dépendances nécessaires avec la commande suivante :

    bash

    pip install undetected_chromedriver selenium

    Téléchargez le chromedriver correspondant à votre système d'exploitation, et mettez à jour la variable driver_path dans le script avec le chemin vers le fichier téléchargé.

Configuration

    Liste de mots-clés principale (list) : Les mots-clés pour lesquels les images seront recherchées.
    Vues associées à chaque terme (views) : Le nombre d'images à extraire pour chaque angle de vue spécifié.
    Chemin du répertoire de destination (folder_path) : Modifiez-le dans la boucle d'itération pour définir l'emplacement où les images seront enregistrées.

Fonctionnement

Le script ouvre une instance du navigateur Chrome avec undetected_chromedriver, effectue une recherche Google Images pour chaque mot-clé et angle de vue spécifiés, puis télécharge les images correspondantes dans un répertoire dédié.

Après chaque itération, le script émet un son de notification et attend l'entrée de l'utilisateur. L'utilisateur peut appuyer sur Enter pour continuer ou saisir 'exit' pour arrêter le script.
Avertissement

    Assurez-vous de respecter les droits d'auteur et les politiques d'utilisation des services en ligne lors du téléchargement et de l'utilisation d'images.
    Le script est conçu pour une utilisation éthique et légale. L'auteur n'est pas responsable de toute utilisation abusive ou illégale du script.

Remarques

    Le script est configuré pour une utilisation sous Windows en raison de l'utilisation de la bibliothèque winsound.
    L'utilisation de méthodes automatisées pour accéder aux services en ligne peut violer les conditions d'utilisation des services. Assurez-vous de vous conformer aux politiques des sites Web que vous consultez.
    Utilisez ce script de manière responsable et respectez la vie privée et les droits d'auteur des autres.
