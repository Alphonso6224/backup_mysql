import subprocess
import configparser
from datetime import datetime, timedelta
import time
import schedule

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
 
 
def shedule_backup() :
    #   Definition des heures de début et de fin de la planification
    start_time = datetime.strptime("07:00", "%H:%M")
    end_time = datetime.strptime("23:59", "%H:%M")
    
    #   Heure de démarrage initial
    current_time = start_time
    
    # Planification de l'exécution toutes les 3 heures
    while current_time <= end_time - timedelta(hours=3):
        schedule.every().day.at(current_time.strftime("%H:%M")).do(run_backup_with_pause, config_file)
        current_time += timedelta(hours=3)
    
    # Planification de l'exécution à 23h, même si une pause est en cours
    schedule.every().day.at("23:00").do(run_backup_with_pause, config_file)
        
    # Exécutez la planification en continu
    while True:
        schedule.run_pending()
        time.sleep(1)
     
     
def run_backup_with_pause(config_file):
    # Exécute la sauvegarde
    backup_mysql(config_file)
    
    # Pause de 3 heures
    time.sleep(3 * 60 * 60)  # 3 heures en secondes              
#   Exemple d'utilisation
if __name__ == "__main__":
    config_file = 'config.ini'
    run_backup_with_pause(config_file)