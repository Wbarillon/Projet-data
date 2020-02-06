'''
Ce code sert à importer des fichiers dans la base de données de Django. Il n'est pas très efficace dans la mesure où il faut importer les fichiers un à un, mais pour le projet, il a suffit.
Il n'est pas efficace dans le sens où il faut le modifier à chaque fois qu'on souhaite importer un fichier, à 3 endroits différents : 
-   dans le tableau data où il faut rentrer les en-têtes des colonnes
-   dans le chemin d'accès au fichier, où il faut donner le nom du fichier
-   dans boucle, où la variable objet fait référence à la classe employée comme models (accessoirement, il faut importer le model)
'''

from django.core.management.base import BaseCommand, CommandError
import csv

from hatvp_app.models import Organigramme

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        # Pour effacer puis réécrire dans la base de donnée, au cas où on importe plusieurs fois le même fichier
        # Dirigeants.objects.all().delete()

        data = [
            'fonction_collaborateur',
            'representants_id',
            'collaborateur'
        ]

        with open("D:/Users/Sajtis/Documents/HETIC/MD4 P2021/1-Code/mes_projets/hatvp_project/hatvp_app/datasets/df_organigramme_118.csv",encoding = "utf8") as csvfile:

            # Plutôt que d'importer des csv, on peut importer des dataframes : au lieu de boucler sur spamreader, boucler sur dataframe
            spamreader = csv.reader(csvfile, delimiter=';')
            next(spamreader,None)
            for row in spamreader:
                obj = Organigramme()
                for tab in range(len(data)):
                    setattr(obj, data[tab], row[tab])
                obj.save()

        print("--------------- Fin remplissage reader test ---------------")