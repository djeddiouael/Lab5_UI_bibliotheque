
from django.contrib import admin
from .models import Auteur, Livre, Emprunt

admin.site.register(Auteur)
admin.site.register(Livre)
admin.site.register(Emprunt)