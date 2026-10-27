# TP4 – Interface Graphique pour une API REST Django

Ce projet est réalisé dans le cadre des travaux pratiques du module **WAMS**, en Master 1 GL, Semestre 3, à l’Université M’hamed Bougara de Boumerdès (UMBB).

L’objectif est de développer une interface web permettant d’interagir avec une API REST Django de gestion de bibliothèque. Cette interface communique avec l’API pour gérer les auteurs, les livres et les emprunts, sans accéder directement à la base de données.

## 🎯 Objectifs du TP

- Développer une interface graphique web avec Django.
- Interagir avec une API REST à l’aide de requêtes HTTP.
- Afficher et gérer les auteurs, les livres et les emprunts.
- Implémenter les opérations CRUD : création, consultation, modification et suppression.
- Organiser les templates HTML, les fichiers CSS et JavaScript.
- Mettre en place une navigation entre les différentes pages.
- Vérifier les opérations effectuées via l’interface d’administration Django.

## 🛠️ Technologies utilisées

- **Python** – Langage de programmation
- **Django** – Framework web
- **Django REST Framework** – API REST (si utilisé dans le TP3)
- **HTML5** – Structure des pages
- **CSS3** – Mise en forme
- **JavaScript** – Appels HTTP vers l’API
- **SQLite ou autre base configurée** – Persistance des données

## 📂 Structure du projet

```text
TP4-Django-REST-UI/
├── manage.py
├── settings.py
├── urls.py
├── templates/
│   └── bib/
│       ├── base.html
│       ├── auteurs.html
│       ├── livres.html
│       └── emprunts.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── UI_bibliotheque/
│   ├── views.py
│   ├── urls.py
│   └── ...
└── README.md
```

*Remarque : cette structure est indicative. Elle doit être adaptée à l’organisation réelle du projet TP3 et de l’application Django.*

## 📚 Fonctionnalités

### 1. Gestion des auteurs

La page `/auteurs/` permet de :

- Afficher la liste des auteurs récupérés depuis l’API `/api/auteurs/`.
- Ajouter un auteur à l’aide d’un formulaire.
- Envoyer une requête `POST` pour créer un auteur.
- Supprimer un auteur à l’aide d’une requête `DELETE`.

### 2. Gestion des livres

La page `/livres/` permet de :

- Afficher la liste des livres.
- Ajouter un livre via une requête `POST` vers `/api/livres/`.
- Supprimer un livre avec une requête `DELETE`.
- Modifier un livre avec une requête `PUT`.

### 3. Gestion des emprunts

La page `/emprunts/` permet de :

- Afficher la liste des emprunts.
- Consulter les informations du livre, de l’auteur, de la date d’emprunt et de la date de retour.
- Enregistrer un nouvel emprunt via une requête `POST`.
- Marquer un emprunt comme retourné via une requête `PUT`.

## 🧭 Navigation

Une barre de navigation commune est intégrée dans `base.html` afin de faciliter l’accès aux différentes pages :

- `/auteurs/`
- `/livres/`
- `/emprunts/`

Le template `base.html` centralise la structure commune des pages : en-tête, navigation, contenu principal et pied de page.

## ⚙️ Installation et exécution

### Prérequis

- Python 3
- pip
- Django
- Le projet API REST du TP3

### 1. Cloner le dépôt

```bash
git clone <URL_DU_DEPOT>
cd <NOM_DU_DEPOT>
```

Remplacez les valeurs entre chevrons par l’URL et le nom réels de votre dépôt.

### 2. Créer un environnement virtuel

```bash
python -m venv venv
```

Activer l’environnement :

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Installer les dépendances

Si le projet contient un fichier `requirements.txt` :

```bash
pip install -r requirements.txt
```

Sinon, installez les dépendances nécessaires selon la configuration du projet, notamment Django et éventuellement Django REST Framework.

### 4. Configurer les templates et les fichiers statiques

Dans `settings.py`, configurez les dossiers `templates` et `static` conformément à la structure réelle du projet.

Exemple :

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES[0]["DIRS"] = [BASE_DIR / "templates"]

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
```

Adaptez cette configuration si le projet utilise déjà d’autres chemins.

### 5. Lancer le serveur Django

```bash
python manage.py migrate
python manage.py runserver
```

Ouvrez ensuite :

`http://127.0.0.1:8000/`

**Important :** les migrations ne sont nécessaires que si la configuration du projet l’exige. L’API REST du TP3 doit être opérationnelle et les routes doivent correspondre à celles utilisées par l’interface.

## 🔗 Communication avec l’API REST

L’interface utilise des requêtes HTTP pour interagir avec les endpoints de l’API.

| Opération | Méthode HTTP | Endpoint |
|---|---|---|
| Consulter les auteurs | `GET` | `/api/auteurs/` |
| Ajouter un auteur | `POST` | `/api/auteurs/` |
| Supprimer un auteur | `DELETE` | Endpoint détaillé de l’auteur |
| Consulter les livres | `GET` | `/api/livres/` |
| Ajouter un livre | `POST` | `/api/livres/` |
| Modifier un livre | `PUT` | Endpoint détaillé du livre |
| Consulter les emprunts | `GET` | Endpoint des emprunts |
| Ajouter un emprunt | `POST` | Endpoint des emprunts |
| Marquer un emprunt comme retourné | `PUT` | Endpoint détaillé de l’emprunt |

Les endpoints détaillés dépendent des routes définies dans l’API du TP3.

## 🧪 Tests et validation

Les tests portent notamment sur :

- L’affichage des données provenant de l’API.
- La création et la suppression d’auteurs.
- La création, la modification et la suppression de livres.
- La création et la mise à jour des emprunts.
- La navigation entre les pages.
- La cohérence des données avec la base de données, vérifiée via l’administration Django.

L’interface doit communiquer avec les données exclusivement par l’intermédiaire de l’API REST, sans accès direct à la base de données depuis l’interface graphique.

## 🎓 Informations académiques

- **Université :** Université M’hamed Bougara de Boumerdès (UMBB)
- **Faculté :** Faculté des Sciences
- **Département :** Informatique
- **Formation :** Master 1 GL
- **Semestre :** Semestre 3
- **Module :** WAMS
- **Travaux pratiques :** TP4 – Interface Graphique pour une API REST Django

## 👤 Auteur

**Ouael DJEDDI**

- GitHub : [@djeddiouael](https://github.com/djeddiouael)

## 📄 Licence

Aucune licence n’est spécifiée pour le moment. Ajoutez un fichier `LICENSE` si vous souhaitez définir les conditions de réutilisation du projet.
