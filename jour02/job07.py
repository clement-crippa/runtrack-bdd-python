import mysql.connector

class CRUD:
    def __init__(self, host, user, password, database):
        self.bdd = mysql.connector.connect(host=host, user=user, password=password, database=database)

    def Afficher_Employes(self):
        cursor = self.bdd.cursor()
        cursor.execute("select * from employes;")
        for employes in cursor:
            print(employes)

    def Afficher_Employes3K(self):
        cursor = self.bdd.cursor()
        cursor.execute("select * from employes where salaire>3000;")
        for salaire in cursor:
            print("Voici les employés ayant un salaire supérieur a 3000€:", salaire[1], salaire[2], salaire[3], "€")

    def Afficher_Employes_Services(self):
        cursor = self.bdd.cursor()
        cursor.execute("select e.*, s.nom from employes e inner join services s on e.id_service = s.id;")
        for x in cursor:
            print(x)

    def Supprimer_Employes(self, id):
        cursor = self.bdd.cursor()
        cursor.execute("delete from employes where id=(%s);", (id,))
        self.bdd.commit()


    def Ajouter_Employes(self, nom, prenom, salaire, id_service):
        cursor = self.bdd.cursor()
        cursor.execute("insert into employes (nom,prenom,salaire,id_service) values (%s, %s, %s, %s);",
                       (nom, prenom, salaire, id_service))
        self.bdd.commit()

    def Modifier_Salaire(self, id, salaire):
        cursor = self.bdd.cursor()
        cursor.execute("update employes set salaire=(%s) where id=(%s);", (salaire, id,))
        self.bdd.commit()


    def Fermer_Session(self):
        cursor= self.bdd.cursor()
        cursor.close()


crud = CRUD("localhost", "root", "rootmdp", "laplateforme")
crud.Afficher_Employes()
crud.Afficher_Employes3K()
print("---------------------")
crud.Ajouter_Employes("Bobbyne", "Bobby", 2500, 1)
crud.Afficher_Employes()
print("---------------------------")
crud.Afficher_Employes_Services()
print("------------------------")
crud.Modifier_Salaire(23, 3500)
crud.Afficher_Employes3K()

crud.Fermer_Session()
