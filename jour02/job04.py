import mysql.connector

# Connexion a la base de donnée
bdd = mysql.connector.connect(host="localhost", user="root", password="rootmdp", database="LaPlateforme")
# Création d'un curseur
cursor = bdd.cursor()
# Requête pour demander le nom des salles et leur capacité dans la table salles
cursor.execute("select nom,capacite from salles;")
# Affiche les noms et leur capacité
for salles in cursor:
    print(salles)
# Fermeture de la session
cursor.close()