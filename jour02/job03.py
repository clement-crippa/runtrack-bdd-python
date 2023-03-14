import mysql.connector

# Connexion a la base de donnée
bdd = mysql.connector.connect(host="localhost", user="root", password="rootmdp", database="LaPlateforme")
# Création d'un curseur
cursor = bdd.cursor()
# Création des objets dans la table étage
cursor.execute("insert into etage (nom,numero,superficie) values ('RDC',0,500),('R+1',1,500);")
# Création des objets dans la table salles
cursor.execute("insert into salles (nom,id_etage,capacite) values ('Lounge',1,100),('Studio Son',1,5),('Broadcasting',2,50),('Bocal Peda',2,4),('Coworking',2,80),('Studio Video',2,5);")
# Fermeture de la session
cursor.close()