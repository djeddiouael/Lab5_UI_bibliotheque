from django.db import models



class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    nationalite = models.CharField(max_length=100)
    date_naissance = models.DateField()

    def __str__(self):
        return self.nom + " " + self.prenom


class Livre(models.Model):
    titre = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20)
    date_publication = models.DateField()
    nombre_pages = models.IntegerField()
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titre


class Emprunt(models.Model):
    nom_lecteur = models.CharField(max_length=100)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    date_emprunt = models.DateField()
    date_retour = models.DateField(null=True, blank=True)
    retourne = models.BooleanField(default=False)

    def __str__(self):
        return self.nom_lecteur