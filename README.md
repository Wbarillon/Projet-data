# Projet-data
Code conçu au cours du projet-data du 27 au 31 janvier.

Les différents détails concernant la conception du code se trouvent en commentaire de chacun des fichiers concernés.
Django étant un cadriciel, la plupart des fichiers sont les mêmes et se ressemblent. La liste suivante présente les fichiers remarquables de ce projet :

**Dans le dossier "hatvp_app" :**
- 1° : management\commands\import.py
- 2° : admin.py
- 3° : models.py
- 4° : urls.py
- 5° : views.py

**Dans le dossier "hatvp_project" :**
- 1° : urls.py

**Comment tester l'application ?**

Parmi les "datasets" présents, importer le fichier df_organigramme_118.csv dans la base de données.

Liste des commandes pour effectuer l'importation (sous Windows 10) :

```
py manage.py makemigrations
py manage.py migrate
py manage.py import
```

Source : https://docs.djangoproject.com/fr/3.0/topics/migrations/

Une fois le serveur lancé, la page d'acceuil par défaut présente une barre de recherche avec un bouton. Appuyer sur le bouton suffit pour rediriger vers les données affichées.

Commande pour lancer le serveur (sous Windows 10):

```
py manage.py runserver
```

**Concernant les templates et l'intégration du HTML / CSS :**

Cette partie de l'application est opérationnelle, mais pas reproductible. Les différentes parties qui composent la page HTML n'ont pas été organisés en composants. Les règles de css sont contenues dans deux fichiers css. Si dans la version actuelle du projet aucun conflit entre ces règles n'existent, l'organisation actuelle amène nécessairement à des conflits si on souhaite continuer à améliorer la partie front-end.

Ne me demander pas pourquoi j'ai pas simplement fait un seul fichier comme j'ai l'habitude de faire...
