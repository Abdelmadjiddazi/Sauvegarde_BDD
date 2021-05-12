#!usr/bin/env   python
# Script de sauvegarde d'une base de donnée
# Abdelmadjid DAZI crée le 10 mai 2021

#Import des librairies 

import os                     # Import des fichiers et dossiers
import time                   # Import du temps (heure,minute,seconde..)
import datetime               # Import de la date et heure

# Détails de la base de données MySQL vers laquelle la sauvegarde doit être effectuée. Assurez-vous que l'utilisateur ci-dessous a suffisamment de privilèges pour effectuer la sauvegarde des bases de données. 
# Pour faire une sauvegarde de plusieurs bases de données, créez un fichier nommé /backup/dbnames.txt et mettez les noms des bases de données un par ligne et assignez-les à la variable DB_NAME.


DB_HOST = 'localhost'           # Nome de l'host
DB_USER = 'adminuser'           # Nom de l'utilisateur de la base de donnée
DB_USER_PASSWORD = 'root'       # Le mot de passe de l'utilisateur de la base de donnée
    #DB_NAME = '/backup/dbnames.txt'          # Fichier texte regroupant les noms des base de données 
DB_NAME = 'wordpress'           # Nom de la base de donnée
BACKUP_PATH = '/backup/backupdb/' # Chemin dans lequel seront ajoutées les sauvegardes 

    # Obtenir la date actuelle pour créer un dossier de sauvegarde séparé comme "12052021-071334". 
DATETIME = time.strftime('%m%d%Y-%H%M%S')               # Appel de la string strftime pour la date et l'heure

TODAYBACKUPPATH = BACKUP_PATH + DATETIME                # Création du dossier de sauvegarde avec l'heure et la date

    # Vérifier si le dossier de sauvegarde existe déjà ou non. S'il n'existe pas, il sera créé. 
print "Création du dossier de sauvegarde" 
if not os.path.exists(TODAYBACKUPPATH): # Si le dossier n'existe pas alors
        os.makedirs(TODAYBACKUPPATH)    # On le créer

    # Vérifier si on veut prendre une seule sauvegarde de la base de données ou assigner des sauvegardes multiples dans DB_NAME 
print "Check des fichiers de base de donnée" 
if os.path.exists(DB_NAME):             # Si le fichier est présent
        file1 = open(DB_NAME)           # On ouvre le fichier et on check ce qu'il y a dedans
        multi = 1                       # Nous indiquons ici le nombre de base de donnée présente en ajoutant 1 à la variable
        print "fichier de base de donnée trouvés..." 
        print "Lancement de backup de toutes les bases de données du fichiers" + DB_NAME          # Lancement d'une ou des sauvegardes de la/les base de données trouvées
else: 
        print "Fichier de base de donnée introuvable"               # Si aucun fichier de bdd n'est présent 
        print "lancement du backup de la base de donnée " + DB_NAME # Le backup s'effectuera dans DB_NAME
        multi = 0                       # La variable multi obtient 0 si aucun fichier de base de donnée n'est présent

    # Démarrage du processus de sauvegarde de la base de données. 
if multi:                                         # Si multi = 1 alors ouvrir le fichier txt
       in_file = open(DB_NAME,"r")                
       flength = len(in_file.readlines())         # Va lire les lignes qui sont présentes dans le fichier
       in_file.close()                            # Ferme le fichier
       i = 1                                      # on déclare une variable i
       dbfile = open(DB_NAME,"r")                 # On ouvre le fichier pour le lire

       while i <= flength:          # Tant que i est inférieur ou égal (s'il y a une ligne dans le fichier txt)
           db = dbfile.readline()   # lecture du nom de la base de données à partir du fichier 
           db = db[:-1]             # supprime les lignes supplémentaires 
           dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + TODAYBACKUPPATH + "/" + db + ".sql"   # Fonction dump qui va permettre de générer le fichier de sauvegarde
           os.system(dumpcmd)       # Execute la commande dumpcmd
           i++                      # On incrémente la valeur
       dbfile.close()               # On ferme le ficher
else:                               # Sinon
       db = DB_NAME                 # On prend la seul Base de donnée disponible (ou bien celle que l'on a ajouter au début)
       dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + TODAYBACKUPPATH + "/" + db + ".sql" # Appel de l'utilitaire de commande pour répondre au besoin
       os.system(dumpcmd)           # Execution de la commande dump

print "La sauvegarde du script à été réussie"                                     # On affiche que la sauvegarde est réussie
print "Votre sauvegarde a été créé dans '" + TODAYBACKUPPATH + "' directory"      # On affiche que la sauvegarde est bien disponible dans le dossier/repertoire que l'on a déclaré
