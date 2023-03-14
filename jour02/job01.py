import mysql.connector

# Connexion a la base de donnée
bdd = mysql.connector.connect(host="localhost", user="root", password="rootmdp", database="LaPlateforme")
# Création d'un curseur
cursor = bdd.cursor()
# Exécutions de la commande pour afficher les informations de la table étudiants
cursor.execute("select * from etudiants")
# Affiche les données de la table étudiants
for etudiants in cursor:
    print(etudiants)
# Ferme la session
cursor.close()
