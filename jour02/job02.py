import mysql.connector

# Connexion a la base de donnée
bdd = mysql.connector.connect(host="localhost", user="root", password="rootmdp", database="LaPlateforme")
# Création d'un curseur
cursor = bdd.cursor()
# Création de la table etage
cursor.execute("create table etage( id int auto_increment Primary key,nom varchar(255),numero int,superficie int);")
# Création de la table salles
cursor.execute("create table salles( id int auto_increment Primary key,nom varchar(255),id_etage int,capacite int);")
# Fermeture de la session
cursor.close()