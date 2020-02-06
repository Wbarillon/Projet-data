'''
Ici, beaucoup de choses ne vont pas :
-   des modèles ne sont pas utilisés
-   des champs sont mal optimisés (TextField pour toutes les chaînes de caractères)
-   les modèles en eux-mêmes n'ont pas vraiment de sens...

La raison pour laquelle les modèles n'ont pas vraiment de sens est que je n'ai pas été en mesure de capter des valeurs directement entré depuis la partie front-end pour rendre les requêtes sur la base de données dynamiques. En conséquence, vous le verrez plus tard dans le fichier views.py, les quelques requêtes via l'orm sont "en durs" dans le fichier. Dans ce contexte, il est inutile d'avoir une base de donnée exhaustive : une base de donnée comprenant les informations nécessaires pour faire fonctionner la requête et afficher ce qui est nécessaire pour la démonstration suffit.
Pour palier à cela, il faudrait complètement revoir la conception des modèles. Le cours de SQL qu'on a eu cette année à une base théorique suffisante pour ce travail.
'''

from django.db import models

# Create your models here.

class Organigramme(models.Model):
    fonction_collaborateur = models.TextField(max_length=300, null=True, blank=True)
    representants_id = models.IntegerField(null=True)
    collaborateur = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.representants_id)

class Organization(models.Model):
    representants_id = models.IntegerField(null=True)
    denomination = models.TextField(max_length=300, null=True, blank=True)
    label_categorie_organisation = models.TextField(max_length=300, null=True, blank=True)
    dirigeant = models.TextField(max_length=300, null=True, blank=True)
    fonction_dirigeant = models.TextField(max_length=300, null=True, blank=True)
    fonction_collaborateur = models.TextField(max_length=300, null=True, blank=True)
    collaborateur = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.collaborateur

class DfTwoFive(models.Model):
    representants_id = models.IntegerField(null=True)
    denomination = models.TextField(max_length=300, null=True, blank=True)
    label_categorie_organisation = models.TextField(max_length=300, null=True, blank=True)
    dirigeant = models.TextField(max_length=300, null=True, blank=True)
    fonction_dirigeant = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.representants_id)

class DfDirigeants(models.Model):
    representants_id = models.IntegerField(null=True)
    dirigeant = models.TextField(max_length=300, null=True, blank=True)
    fonction_dirigeant = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.dirigeant

class InformationsGenerales(models.Model):
    representants_id = models.IntegerField(null=True)
    adresse = models.TextField(max_length=250, null=True, blank=True)
    code_postal = models.TextField(max_length=20, null=True)
    derniere_publication_activite = models.DateTimeField(null=True)
    date_premiere_publication = models.DateTimeField(null=True, blank = True)
    declaration_organisation_appartenance = models.BooleanField(null=True)
    declaration_tiers = models.BooleanField(null=True)
    denomination = models.TextField(max_length=250, null=True, blank=True)
    identifiant_national = models.TextField(max_length=10)
    activites_publiees = models.BooleanField(null=True)
    page_facebook = models.TextField(max_length=300, null=True, blank=True)
    page_linkedin = models.TextField(max_length=300, null=True, blank=True)
    page_twitter = models.TextField(max_length=300, null=True, blank=True)
    site_web = models.TextField(max_length=200, null=True, blank=True)
    nom_usage_HATVP = models.TextField(max_length=50, null=True, blank=True)
    pays = models.TextField(max_length=50, null=True, blank=True)
    sigle_hatvp = models.TextField(max_length=50, null=True, blank=True)
    type_identifiant_national = models.TextField(max_length=15, null=True, blank=True)
    ville = models.TextField(max_length=100, null=True, blank=True)
    label_categorie_organisation = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.identifiant_national)


class Dirigeants(models.Model):
    civilite_dirigeant = models.TextField(max_length=3, null=True, blank=True)
    fonction_dirigeant = models.TextField(max_length=60, null=True, blank=True)
    nom_dirigeant = models.TextField(max_length=30, null=True, blank=True)
    prenom_dirigeant = models.TextField(max_length=30, null=True, blank=True)
    representants_id = models.IntegerField(null=True)
    nom_prenom_dirigeant = models.TextField(max_length=61, null=True, blank=True)

    def __str__(self):
        return str(self.pk)


class Collaborateurs(models.Model):
    civilite_collaborateur = models.TextField(max_length=3, null=True, blank=True)
    fonction_collaborateur = models.TextField(max_length=60, null=True, blank=True)
    nom_collaborateur = models.TextField(max_length=30, null=True, blank=True)
    prenom_collaborateur = models.TextField(max_length=30, null=True, blank=True)
    representants_id = models.IntegerField(null=True)
    nom_prenom_collaborateur = models.TextField(max_length=61, null=True, blank=True)

    def __str__(self):
        return str(self.pk)


class Clients(models.Model):
    representants_id = models.IntegerField(null=True)
    denomination_client = models.TextField(max_length=60, null=True, blank=True)
    identifiant_national_client = models.TextField(max_length=15, null=True, blank=True)
    type_identifiant_national_client = models.TextField(max_length=15, null=True, blank=True)

    def __str__(self):
        return str(self.identifiant_national_client)


class Affiliations(models.Model):
    representants_id = models.IntegerField(null=True)
    denomination_affiliation = models.TextField(max_length=60, null=True, blank=True)
    identifiant_national_affiliation = models.TextField(max_length=15, null=True, blank=True)
    type_identifiant_national_affiliation = models.TextField(max_length=15, null=True, blank=True)

    def __str__(self):
        return str(self.identifiant_national_affiliation)

class NiveauxInterventions(models.Model):
    niveau_intervention = models.TextField(max_length=250, null=True, blank=True)
    representants_id = models.IntegerField(null=True)

    def __str__(self):
        return str(self.pk)


class DomainesInterventionsActionsMenees(models.Model):
    domaines_intervention_actions_menees = models.TextField(max_length=600, null=True, blank=True)
    activite_id = models.IntegerField(null=True)

    def __str__(self):
        return str(self.pk)


class ObjetsActivites(models.Model):
    activite_id = models.IntegerField(null=True)
    exercices_id = models.IntegerField(null=True)
    date_publication_activite = models.DateField(null=True, blank=True)
    identifiant_fiche = models.TextField(max_length=8, null=True, blank=True)
    objet_activite = models.TextField(max_length=800, null=True)

    def __str__(self):
        return str(self.pk)


class SecteursActivites(models.Model):
    secteur_activite = models.TextField(max_length=100, null=True, blank=True)
    representants_id = models.IntegerField(null=True)

    def __str__(self):
        return str(self.pk)


class ActionsMenees(models.Model):
    action_menee = models.TextField(max_length=800, null=True)
    action_representation_interet_id = models.IntegerField(null=True)
    action_menee_autre = models.TextField(max_length=800, null=True)

    def __str__(self):
        return str(self.pk)


class Beneficiaires(models.Model):
    beneficiaire_action_menee = models.TextField(max_length=250, null=True, blank=True)
    action_representation_interet_id = models.IntegerField(null=True)
    action_menee_en_propre = models.BooleanField(null=True)

    def __str__(self):
        return str(self.beneficiaire_action_menee)


class DecisionsConcernees(models.Model):
    decision_concernee = models.TextField(max_length=300, null=True, blank=True)
    action_representation_interet_id = models.IntegerField(null=True)

    def __str__(self):
        return str(self.decision_concernee)


class MinisteresAaiApi(models.Model):
    action_representation_interet_id = models.IntegerField(null=True)
    responsable_public = models.TextField(max_length=300, null=True, blank=True)
    departement_ministeriel = models.TextField(max_length=300, null=True, blank=True)
    responsable_public_ou_dpt_ministeriel_autre = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.responsable_public)


class Observations(models.Model):
    action_representation_interet_id = models.IntegerField(null=True)
    activite_id = models.IntegerField(null=True)
    observation = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.observation)


class Exercices(models.Model):
    exercices_id = models.IntegerField(null=True)
    representants_id = models.IntegerField(null=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    exercice_sans_activite = models.BooleanField(null=True)
    nombre_activites = models.IntegerField(null=True, blank=True)
    declaration_incomplete = models.BooleanField(null=True)
    date_publication = models.DateField(null=True, blank=True)
    exercice_sans_CA = models.BooleanField(null=True)
    montant_depense = models.CharField(max_length=12, null=True, blank=True)
    nombre_salaries = models.FloatField(null=True, blank=True)
    chiffre_affaires = models.CharField(max_length=12, null=True, blank=True)
    annee_debut = models.IntegerField(null=True, blank=True)
    annee_fin = models.IntegerField(null=True, blank=True)
    montant_depense_inf = models.IntegerField(null=True, blank=True)
    montant_depense_sup = models.IntegerField(null=True, blank=True)
    ca_inf = models.IntegerField(null=True, blank=True)
    ca_sup = models.TextField(max_length=12, null=True, blank=True)

    def __str__(self):
        return str(self.pk)
