from django.contrib import admin
from django.urls import path, include
from gestion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('gestion.urls')),
    

    path('', views.accueil, name='accueil'),
    
    
    path('auteurs/', views.afficher_auteurs, name='auteurs_page'),
    path('livres/', views.afficher_livres, name='livres_page'),
    path('emprunts/', views.afficher_emprunts, name='emprunts_page'),
]