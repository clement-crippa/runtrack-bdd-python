import mysql.connector

# Connexion a la base de donnée
bdd = mysql.connector.connect(host="localhost", user="root", password="rootmdp", database="LaPlateforme")
# Création d'un curseur
cursor = bdd.cursor()
# Requête pour demander le total de la superficie de la table etage
cursor.execute("select sum(superficie) from etage;")
# Affiche la superficie total
for etage in cursor:
    print("La superficie de La Plateforme est de :", etage[0], "m²")
# Fermeture de session
cursor.close()
