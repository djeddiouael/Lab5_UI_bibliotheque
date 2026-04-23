from django.urls import path
from . import views

urlpatterns = [
    
    
    path('auteurs-page/', views.afficher_auteurs, name='auteurs_page'),
    path('livres-page/', views.afficher_livres, name='livres_page'),
    path('emprunts-page/', views.afficher_emprunts, name='emprunts_page'),

    

    path('auteurs/', views.liste_auteurs, name='liste_auteurs'),
    path('auteurs/creer/', views.creer_auteur, name='creer_auteur'),
    path('auteurs/<int:id>/', views.detail_auteur, name='detail_auteur'),
    path('auteurs/<int:id>/modifier/', views.modifier_auteur, name='modifier_auteur'),
    path('auteurs/<int:id>/supprimer/', views.supprimer_auteur, name='supprimer_auteur'),

    

    path('livres/', views.liste_livres, name='liste_livres'),
    path('livres/creer/', views.creer_livre, name='creer_livre'),
    path('livres/<int:id>/', views.detail_livre, name='detail_livre'),
    path('livres/<int:id>/modifier/', views.modifier_livre, name='modifier_livre'),
    path('livres/<int:id>/supprimer/', views.supprimer_livre, name='supprimer_livre'),

    

    path('emprunts/', views.liste_emprunts, name='liste_emprunts'),
    path('emprunts/creer/', views.creer_emprunt, name='creer_emprunt'),
    path('emprunts/<int:id>/', views.detail_emprunt, name='detail_emprunt'),
    path('emprunts/<int:id>/modifier/', views.modifier_emprunt, name='modifier_emprunt'),
    path('emprunts/<int:id>/supprimer/', views.supprimer_emprunt, name='supprimer_emprunt'),
]