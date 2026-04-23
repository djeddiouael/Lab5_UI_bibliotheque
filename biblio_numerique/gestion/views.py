from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render
import json
from .models import Auteur, Livre, Emprunt



def accueil(request):
    """Affiche la page d'accueil"""
    return render(request, 'accueil.html')



def afficher_auteurs(request):
    """Affiche la page HTML des auteurs"""
    return render(request, 'auteurs.html')




def liste_auteurs(request):
    """GET : Retourne la liste de tous les auteurs"""
    auteurs = Auteur.objects.all()
    data = [
        {
            'id': auteur.id,
            'nom': auteur.nom,
            'prenom': auteur.prenom,
            'date_naissance': str(auteur.date_naissance),
            'nationalite': auteur.nationalite
        }
        for auteur in auteurs
    ]
    return JsonResponse(data, safe=False)


def detail_auteur(request, id):
    """GET : Retourne les détails d’un auteur spécifique"""
    auteur = get_object_or_404(Auteur, id=id)
    data = {
        'id': auteur.id,
        'nom': auteur.nom,
        'prenom': auteur.prenom,
        'date_naissance': str(auteur.date_naissance),
        'nationalite': auteur.nationalite
    }
    return JsonResponse(data)


def creer_auteur(request):
    """POST : Crée un nouvel auteur"""
    if request.method != 'POST':
        return JsonResponse({'erreur': 'Méthode non autorisée'}, status=405)

    try:
        data = json.loads(request.body)
        auteur = Auteur.objects.create(
            nom=data.get('nom'),
            prenom=data.get('prenom'),
            date_naissance=data.get('date_naissance'),
            nationalite=data.get('nationalite', '')
        )

        return JsonResponse({
            'id': auteur.id,
            'message': 'Auteur créé avec succès'
        }, status=201)

    except Exception as e:
        return JsonResponse({'erreur': str(e)}, status=400)


def modifier_auteur(request, id):
    """PUT : Modifie un auteur existant"""
    if request.method != 'PUT':
        return JsonResponse({'erreur': 'Méthode non autorisée'}, status=405)

    auteur = get_object_or_404(Auteur, id=id)

    try:
        data = json.loads(request.body)

        auteur.nom = data.get('nom', auteur.nom)
        auteur.prenom = data.get('prenom', auteur.prenom)
        auteur.date_naissance = data.get('date_naissance', auteur.date_naissance)
        auteur.nationalite = data.get('nationalite', auteur.nationalite)

        auteur.save()

        return JsonResponse({'message': 'Auteur modifié avec succès'})

    except Exception as e:
        return JsonResponse({'erreur': str(e)}, status=400)


def supprimer_auteur(request, id):
    """DELETE : Supprime un auteur"""
    if request.method != 'DELETE':
        return JsonResponse({'erreur': 'Méthode non autorisée'}, status=405)

    auteur = get_object_or_404(Auteur, id=id)
    auteur.delete()

    return JsonResponse({'message': 'Auteur supprimé avec succès'}, status=204)




def afficher_livres(request):
    """Affiche la page HTML des livres"""
    return render(request, 'livres.html')



def liste_livres(request):
    """GET : Retourne la liste de tous les livres"""
    livres = Livre.objects.all().select_related('auteur')
    data = [
        {
            'id': livre.id,
            'titre': livre.titre,
            'isbn': livre.isbn,
            'date_publication': str(livre.date_publication),
            'nombre_pages': livre.nombre_pages,
            'auteur_id': livre.auteur.id,
            'auteur_nom': f"{livre.auteur.prenom} {livre.auteur.nom}",
            'disponible': livre.disponible
        }
        for livre in livres
    ]
    return JsonResponse(data, safe=False)


def detail_livre(request, id):
    """GET : Retourne les détails d'un livre spécifique"""
    livre = get_object_or_404(Livre, id=id)
    data = {
        'id': livre.id,
        'titre': livre.titre,
        'isbn': livre.isbn,
        'date_publication': str(livre.date_publication),
        'nombre_pages': livre.nombre_pages,
        'auteur_id': livre.auteur.id,
        'auteur_nom': f"{livre.auteur.prenom} {livre.auteur.nom}",
        'disponible': livre.disponible
    }
    return JsonResponse(data)


def creer_livre(request):
    """POST : Crée un nouvel livre"""
    if request.method != 'POST':
        return JsonResponse({'erreur': 'Méthode non autorisée'}, status=405)

    try:
        data = json.loads(request.body)
        auteur = get_object_or_404(Auteur, id=data.get('auteur_id'))
        
        livre = Livre.objects.create(
            titre=data.get('titre'),
            isbn=data.get('isbn'),
            date_publication=data.get('date_publication'),
            nombre_pages=data.get('nombre_pages'),
            auteur=auteur,
            disponible=data.get('disponible', True)
        )

        return JsonResponse({
            'id': livre.id,
            'message': 'Livre créé avec succès'
        }, status=201)

    except Exception as e:
        return JsonResponse({'erreur': str(e)}, status=400)


def modifier_livre(request, id):
    """PUT : Modifie un livre existant"""
    if request.method != 'PUT':
        return JsonResponse({'erreur': 'Méthode non autorisée'}, status=405)

    livre = get_object_or_404(Livre, id=id)

    try:
        data = json.loads(request.body)

        livre.titre = data.get('titre', livre.titre)
        livre.isbn = data.get('isbn', livre.isbn)
        livre.date_publication = data.get('date_publication', livre.date_publication)
        livre.nombre_pages = data.get('nombre_pages', livre.nombre_pages)
        livre.disponible = data.get('disponible', livre.disponible)
        
        if data.get('auteur_id'):
            auteur = get_object_or_404(Auteur, id=data.get('auteur_id'))
            livre.auteur = auteur

        livre.save()

        return JsonResponse({'message': 'Livre modifié avec succès'})

    except Exception as e:
        return JsonResponse({'erreur': str(e)}, status=400)


def supprimer_livre(request, id):
    """DELETE : Supprime un livre"""
    if request.method != 'DELETE':
        return JsonResponse({'erreur': 'Méthode non autorisée'}, status=405)

    livre = get_object_or_404(Livre, id=id)
    livre.delete()

    return JsonResponse({'message': 'Livre supprimé avec succès'}, status=204)




def afficher_emprunts(request):
    """Affiche la page HTML des emprunts"""
    return render(request, 'emprunts.html')



def liste_emprunts(request):
    """GET : Retourne la liste de tous les emprunts"""
    emprunts = Emprunt.objects.all().select_related('livre', 'livre__auteur')
    data = [
        {
            'id': emprunt.id,
            'nom_lecteur': emprunt.nom_lecteur,
            'livre_id': emprunt.livre.id,
            'livre_titre': emprunt.livre.titre,
            'auteur_nom': f"{emprunt.livre.auteur.prenom} {emprunt.livre.auteur.nom}",
            'date_emprunt': str(emprunt.date_emprunt),
            'date_retour': str(emprunt.date_retour) if emprunt.date_retour else None,
            'retourne': emprunt.retourne
        }
        for emprunt in emprunts
    ]
    return JsonResponse(data, safe=False)


def detail_emprunt(request, id):
    """GET : Retourne les détails d'un emprunt spécifique"""
    emprunt = get_object_or_404(Emprunt, id=id)
    data = {
        'id': emprunt.id,
        'nom_lecteur': emprunt.nom_lecteur,
        'livre_id': emprunt.livre.id,
        'livre_titre': emprunt.livre.titre,
        'auteur_nom': f"{emprunt.livre.auteur.prenom} {emprunt.livre.auteur.nom}",
        'date_emprunt': str(emprunt.date_emprunt),
        'date_retour': str(emprunt.date_retour) if emprunt.date_retour else None,
        'retourne': emprunt.retourne
    }
    return JsonResponse(data)


def creer_emprunt(request):
    """POST : Crée un nouvel emprunt"""
    if request.method != 'POST':
        return JsonResponse({'erreur': 'Méthode non autorisée'}, status=405)

    try:
        data = json.loads(request.body)
        livre = get_object_or_404(Livre, id=data.get('livre_id'))
        
        emprunt = Emprunt.objects.create(
            nom_lecteur=data.get('nom_lecteur'),
            livre=livre,
            date_emprunt=data.get('date_emprunt'),
            date_retour=data.get('date_retour'),
            retourne=data.get('retourne', False)
        )

        return JsonResponse({
            'id': emprunt.id,
            'message': 'Emprunt créé avec succès'
        }, status=201)

    except Exception as e:
        return JsonResponse({'erreur': str(e)}, status=400)


def modifier_emprunt(request, id):
    """PUT : Modifie un emprunt existant (marquer comme retourné)"""
    if request.method != 'PUT':
        return JsonResponse({'erreur': 'Méthode non autorisée'}, status=405)

    emprunt = get_object_or_404(Emprunt, id=id)

    try:
        data = json.loads(request.body)

        emprunt.nom_lecteur = data.get('nom_lecteur', emprunt.nom_lecteur)
        emprunt.date_emprunt = data.get('date_emprunt', emprunt.date_emprunt)
        emprunt.date_retour = data.get('date_retour', emprunt.date_retour)
        emprunt.retourne = data.get('retourne', emprunt.retourne)

        emprunt.save()

        return JsonResponse({'message': 'Emprunt modifié avec succès'})

    except Exception as e:
        return JsonResponse({'erreur': str(e)}, status=400)


def supprimer_emprunt(request, id):
    """DELETE : Supprime un emprunt"""
    if request.method != 'DELETE':
        return JsonResponse({'erreur': 'Méthode non autorisée'}, status=405)

    emprunt = get_object_or_404(Emprunt, id=id)
    emprunt.delete()

    return JsonResponse({'message': 'Emprunt supprimé avec succès'}, status=204)