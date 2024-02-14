import subprocess
import configparser
from datetime import datetime

def backup_mysql(config_file):
    #   Lecture des informations de configuration depuis le fichier
    config = configparser.ConfigParser()
    config.read(config_file)
    host = config.get('mysql', 'host')
    username = config.get('mysql', 'username')
    password = config.get('mysql', 'password')
    database= config.get('mysql', 'database')
    output_dir = config.get('mysql', 'output_dir')
    
    #   Nom du fichier de sauvegarde avec la date et l'heure actuelles
    backup_filename = f"backup_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.sql"
    backup_path = f"{output_dir}/{backup_filename}"
    
    #   Commande mysqldump pour sauvegarder la base de données
    command = [
        'mysqldump',
        '-h', host,
        '-u', username,
        '-p' + password,
        database
    ]
    
    #   Exécution de la commande et redirection vers un fichier
    try:
        with open(backup_path, 'w') as f:
            subprocess.run(command, stdout=f, check=True)
        print(f"Sauvegarde de la base de données {database} réussie dans {backup_path}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la sauvegarde de la base de données {database}: {e}")
        
#   Exemple d'utilisation
if __name__ == "__main__":
    config_file = 'config.ini'
    backup_mysql(config_file)