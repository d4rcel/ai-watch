# ai-watch

## Présentation

**ai-watch** est un projet de veille automatisée qui collecte des articles depuis des flux RSS, les transforme et les stocke dans une feuille Google Sheets.

## Prérequis

- Python 3.10 ou supérieur
- Un compte Google Cloud avec accès à l'API Google Sheets
- Un environnement virtuel Python (recommandé)

## Installation

1. **Cloner le dépôt**

```bash
git clone <url-du-repo>
cd ai-watch
```

2. **Créer et activer un environnement virtuel**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

## Configuration

1. **Obtenir les identifiants Google Cloud**
   - Télécharger le fichier json des identifiants [Identifiants JSON](https://drive.google.com/drive/folders/17Qz_00bfaZntsoe33S4Pk8ssUG5ZWkrl?usp=sharing).
   - Placer le fichier téléchargé, "veille-ia-466020-2ab42092bf21.json" à la racine du projet
   - Ouvrir le [Google Sheet](https://docs.google.com/spreadsheets/d/1QbA7u_hplBiYBRf4MW-KR-2Onh32PVqdh-s0DRoqBhc/edit?usp=sharing) qui stockera les données (Il est vide par défaut)
   

2. **Configurer les variables d'environnement**
   - Créer le fichier `.env` à la racine du projet
   - Copiez l'entièreté du fichier `.env.example` dans le fichier `.env` :
    
   ```bash
     GOOGLE_APPLICATION_CREDENTIALS : Chemin vers le fichier JSON d\'identifiants.
     GOOGLE_SHEET_NAME : Nom de la feuille Google Sheets.
     SPREADSHEET_KEY : Clé du document Google Sheets.
     RSS_FEEDS : Liste des flux RSS séparés par des virgules.
     REFRESH_INTERVAL_MINUTES : Fréquence de rafraîchissement pour faire tourner l\'agent sans interruption.
     ```
   

3. **Sécurité**
   - Le fichier d'identifiants Google (`.json`) est fourni pour faciliter la configuration et l'exécution du projet.
   - Il ne devrait pas être fourni dans un projet réel.

## Lancement du projet

```bash
python app.py
```

Le script va :
- Lire les flux RSS configurés
- Transformer les données
- Les enregistrer dans la feuille Google Sheets
- Répéter l'opération à l'intervalle défini

## Choix techniques

- **Python** : Simplicité et richesse de l'écosystème pour le traitement de données et l'automatisation.
- **Google Sheets API** : Permet de stocker et partager facilement les résultats de la veille.
- **.env** : Séparation claire des paramètres sensibles et de configuration.
- **Architecture modulaire** :
  - `src/collectors` : Collecte des données (ex : RSS)
  - `src/transformers` : Transformation/filtrage des données
  - `src/storage` : Stockage (Google Sheets)
  - `src/scheduler.py` : Orchestration périodique

## Processus global

1. **Collecte** : Récupération des articles via RSS
2. **Transformation** : Nettoyage et structuration des données
3. **Stockage** : Insertion dans Google Sheets
4. **Automatisation** : Boucle de veille à intervalle régulier

## Tests

Des tests unitaires sont disponibles dans le dossier `tests/` pour valider les principaux modules du projet (collecte RSS, transformation des données, stockage Google Sheets). Vous pouvez les exécuter avec :

```bash
python -m unittest discover tests
```

## Procédé

- Afin de faciliter l'exécution du programme, j'ai créé en amont un projet sur [Google Cloud](https://console.cloud.google.com)
- Dans ce projet, j'ai activé les clés API `Google Sheets API` et `Google Drive API` et créer une clé JSON 
- L'adresse mail du compte de service qui a permi de créer la clé JSON a été ajouté au Google Sheets qui stocke les données, afin de l'ouvrir et d'y écrire plus tard lors de la collecte 
- Au niveau du code, dans un premier temps, je récupère les données (titre, résumé, soure, etc..) des flux RSS du fichier `.env`
- Ensuite, je les formate afin qu'ils matchent le format des données du Google Sheet
- Ensuite, j'insère ces données le Google Sheet

## Remarques

- Ce projet est fourni à titre de démonstration technique.
- Les identifiants Google que j'ai fourni sont uniquement dans l'intention de faciliter l'exécution du programme. Dans un projet réel, Ils ne devraient jamais être inclus pour des raisons de sécurité.
- Normalement, vous devriez générer la clé JSON et activé les clés APIS dans un projet Google Cloud vous-même

## Pistes d'amélioration

- Gérer plusieurs flux RSS et feuilles Google Sheets dynamiquement.
- Ajouter une interface web pour visualiser et gérer la veille.
- Mettre en place un système de notifications (email, Slack, etc.).
- Déployer le projet sur un serveur ou via Docker pour une exécution continue.
- Ajouter la gestion des logs et une meilleure gestion des erreurs.

