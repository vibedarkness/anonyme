from django.db import models

# Create your models here.



class Client(models.Model):

    prenom = models.CharField(max_length = 150, default='', null=True)
    nom = models.CharField(max_length = 150, default='', null=True)
    adresse = models.CharField(max_length = 150, default='', null=True)
    somme = models.IntegerField()

    def __str__(self):
        return self.prenom 




class Transactions(models.Model):
    client=models.ForeignKey(Client, on_delete=models.CASCADE, default='', null=True)
    montant = models.IntegerField()
    
    def __str__(self):
        return self.nom

