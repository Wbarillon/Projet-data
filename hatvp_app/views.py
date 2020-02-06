'''
Comme expliqué plus tôt dans le fichier models.py, les requêtes sur la base de données sont codés... ici.
La page sca_hygiene_products existe bel et bien, mais n'est accessible que via l'url (et ne sert pas à grand chose). Dans sa requête, le filtre est plus "fin". C'est le seul moyen que j'ai trouvé pour éviter que les informations ne s'affiche en chaîne dans la page html - car il n'y a qu'une seule MMe BERGUE dans la base de données).
Quant à l'erreur sur les models, elle est négligeable car ne gêne en rien le fonctionnement du code - du moins, de ma perspective.
'''

from django.shortcuts import render, get_object_or_404

from .models import Organization
from hatvp_app.models import Organigramme

# Create your views here.

def index(request):
    template = 'hatvp_app/index.html'
    return render(request, template, {})

def tableau_blanc(request):
    template = 'hatvp_app/tableau_blanc.html'
    return render(request, template, {})

def rivington(request):
    template = 'hatvp_app/rivington.html'

    query = Organigramme.objects.filter(representants_id = 118)
    # orm_req = request.GET
    # query = Dirigeants.objects.filter(representants_id = orm_req.values())
    return render(request, template, {'items': query})

def sca_hygiene_products(request):
    template = 'hatvp_app/sca_hygiene_products.html'

    query = Organization.objects.filter(representants_id = 25).filter(collaborateur = 'MME BERGUE Elvina')
    # orm_req = request.GET
    # query = Dirigeants.objects.filter(representants_id = orm_req.values())
    return render(request, template, {'items': query})

