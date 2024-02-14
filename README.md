Voici la mise à jour du README pour inclure les instructions sur l'installation du module `schedule` :

---

# Script de Sauvegarde de Base de Données MySQL

Ce script Python vous permet de sauvegarder une base de données MySQL en utilisant l'utilitaire `mysqldump`.

## Prérequis

- Python 3.x installé sur votre système.
- Accès à une base de données MySQL que vous souhaitez sauvegarder.
- Le module Python `configparser` doit être installé si vous souhaitez utiliser un fichier de configuration.
- Le module Python `schedule` doit être installé pour la planification des sauvegardes.

## Installation des Dépendances

```bash
pip install configparser schedule
```

## Configuration

1. Créez un fichier `config.ini` à la racine du projet avec les informations suivantes :

```ini
[mysql]
host = localhost
username = votre_utilisateur
password = votre_mot_de_passe
database = votre_base_de_donnees
output_dir = /chemin/vers/dossier/de/sauvegarde
```

Assurez-vous de remplacer les valeurs par les informations de votre base de données.

2. Si vous préférez spécifier le mot de passe dans une variable d'environnement, vous pouvez laisser le champ `password` vide dans le fichier `config.ini`.

## Utilisation

Exécutez le script `backup_mysql.py` pour sauvegarder votre base de données MySQL :

```bash
python backup_mysql.py
```

Le script générera un fichier de sauvegarde au format SQL dans le répertoire spécifié dans `output_dir`.

## Remarques

- Assurez-vous que le chemin spécifié dans `output_dir` est accessible en écriture par l'utilisateur exécutant le script.
- Ce script utilise `mysqldump` pour effectuer la sauvegarde. Assurez-vous que l'utilitaire `mysqldump` est installé sur votre système et accessible dans le chemin.

---