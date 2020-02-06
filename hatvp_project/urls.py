"""hatvp_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

'''
Plutôt que d'enregistrer les urls du projet dans ce fichier, ce fichier fait référence à un autre fichier urls.py qui se trouve au niveau de l'application. Cette organisation permet d'améliorer la lisibilité des urls, notamment dans le cas où plusieurs applications partagent la même configuration d'un seul projet.
'''

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hatvp_app.urls')),
]
