from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('tableau_blanc/', views.tableau_blanc, name = 'tableau_blanc'),
    path('rivington/', views.rivington, name = 'rivington'),
    path('sca_hygiene_products/', views.sca_hygiene_products, name = 'sca_hygiene_products')
]