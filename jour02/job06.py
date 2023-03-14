import mysql.connector

# Connexion a la base de donnée
bdd = mysql.connector.connect(host="localhost", user="root", password="rootmdp", database="LaPlateforme")
# Création d'un curseur
cursor = bdd.cursor()
# Requête pour demander le total de la superficie de la table salles
cursor.execute("select sum(capacite) from salles;")
# Affiche la superficie total
for salles in cursor:
    print("La capacité de toute les salles est de :", salles[0])
# Fermeture de session
cursor.close()
