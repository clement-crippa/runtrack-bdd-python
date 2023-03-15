import mysql.connector

class Zoo:
    def __init__(self, host, user, password, database):
        self.bdd = mysql.connector.connect(host=host, user=user, password=password, database=database)

    def Afficher_Animal(self):
        cursor = self.bdd.cursor()
        cursor.execute("select * from animal;")
        for animal in cursor:
            print(animal)


    def Afficher_Animal_Cage(self):
        cursor = self.bdd.cursor()
        cursor.execute("select a.*, c.nom from animal a inner join cage c on a.id_cage = c.id;")
        for x in cursor:
            print(x)
    def Superficie(self):
        cursor=self.bdd.cursor()
        cursor.execute("select sum(superficie) from cage;")
        for superficie in cursor:
            print("La superficie total de toute les cages est de",superficie[0],"m²")
    def Supprimer_Animal(self, id):
        cursor = self.bdd.cursor()
        cursor.execute("delete from animal where id=(%s);", (id,))
        self.bdd.commit()
    def Ajouter_Cage(self,superficie, id_cage,capacite):
        cursor = self.bdd.cursor()
        cursor.execute("insert into cage (superficie,id_cage,capacite) values (%s, %s, %s);",(superficie,id_cage,capacite))
        self.bdd.commit()


    def Ajouter_Animal(self, nom, race, id_cage, naissance,origine):
        cursor = self.bdd.cursor()
        cursor.execute("insert into animal (nom,race,id_cage,naissance,origine) values (%s, %s, %s, %s,%s);",(nom, race, id_cage, naissance,origine))
        self.bdd.commit()


    def Deplacer_Animal(self, id_cage, id):
        cursor = self.bdd.cursor()
        cursor.execute("update animal set id_cage=(%s) where id=(%s);", (id_cage, id,))
        self.bdd.commit()


    def Fermer_Session(self):
        cursor= self.bdd.cursor()
        cursor.close()


zoo = Zoo("localhost", "root", "rootmdp", "laplateforme")
zoo.Ajouter_Animal("Lion","Sauvage",1,1998,"Australie")
zoo.Ajouter_Animal("Renard","Sauvage",1,1999,"Australie")
zoo.Ajouter_Animal("Singe","Sauvage",2,2000,"France")
print("-----------------")
zoo.Afficher_Animal()
print("-------------------")
zoo.Ajouter_Cage(1000,1,4)
zoo.Ajouter_Cage(200,2,2)
zoo.Superficie()
print("------------------")
zoo.Afficher_Animal_Cage()
print("------------------")
zoo.Deplacer_Animal(2,1)
zoo.Afficher_Animal_Cage()
print("-----------------")
zoo.Fermer_Session()