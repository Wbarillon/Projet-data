'''
Ce code n'est pas très pratique et pourrait être amélioré de façon à pouvoir enregistrer automatiquement les models écrit dans le fichier models.py. Cela éviterait de se préoccuper de ce fichier et se concentrer sur des tâches plus importantes.

Il faudrait importer le fichier model directement et trouver un moyen d'enregistrer les models de manière dynamique.
'''

from django.contrib import admin

from .models import DfDirigeants
from .models import DfTwoFive
from .models import Organization
from .models import Organigramme

# Register your models here.

admin.site.register(DfDirigeants)
admin.site.register(DfTwoFive)
admin.site.register(Organization)
admin.site.register(Organigramme)

