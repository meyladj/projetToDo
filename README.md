README.md pour Focus to do

Contributeurs
Ce projet a été réalisé grâce à la collaboration de l'équipe suivante :

Ladjabi Mey Khadidja - Développeuse principale + Contributrice Backend
Aitamer Louizette - Contributrice frontend
Hamouri Céline - presentation + Base de données
Chaour Lina - Contributrice frontend
Introduction: 

Bienvenue dans ce projet Django ! Cette application utilise plusieurs dépendances modernes et est conçue pour être facilement configurable. Suivez les étapes ci-dessous pour configurer l'environnement et exécuter le projet.

Prérequis
Python : Assurez-vous d'avoir Python 3.9 ou une version plus récente.
MySQL : Le projet utilise MySQL comme base de données. Installez MySQL Server si ce n'est pas déjà fait.
Git : Assurez-vous que Git est installé sur votre machine pour cloner le dépôt.

Installation

1. Cloner le projet
Utilisez Git pour cloner ce dépôt sur votre machine locale :

git clone https://github.com/votre-utilisateur/votre-repo.git
Naviguez dans le répertoire du projet :
cd votre-repo

2. Créer un environnement virtuel
Créez un environnement virtuel pour isoler les dépendances Python :

python -m venv venv
Activez l'environnement virtuel :

Sur Windows :
venv\Scripts\activate

Sur macOS/Linux :
source venv/bin/activate


3. Installer les dépendances
Toutes les dépendances nécessaires sont listées dans le fichier requirements.txt. Installez-les en exécutant :
pip install -r requirements.txt

4. Configurer les variables d'environnement
Créez un fichier .env à la racine du projet et ajoutez-y les informations sensibles :
SECRET_KEY=remplacez_par_votre_clé_secrète
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_NAME=nom_de_votre_base_de_données
DATABASE_USER=utilisateur_mysql
DATABASE_PASSWORD=mot_de_passe_mysql
DATABASE_HOST=localhost
DATABASE_PORT=3306

5. Configurer la base de données
Assurez-vous que votre base de données MySQL est en cours d'exécution et créez la base de données :
CREATE DATABASE nom_de_votre_base_de_données;
Ensuite, appliquez les migrations pour créer les tables nécessaires :
python manage.py makemigrations
python manage.py migrate

6. Créer un superutilisateur
Créez un administrateur pour accéder à l'interface 
d'administration Django :
python manage.py createsuperuser
Lancer le projet

Exécutez le serveur de développement Django :
python manage.py runserver
Le projet sera disponible à l'adresse http://127.0.0.1:8000/.
