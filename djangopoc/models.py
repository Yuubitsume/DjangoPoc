from django.db import models

class Voiture(models.Model):
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    annee_construction = models.IntegerField()
    cylindree = models.IntegerField()
    version = models.CharField(max_length=100)
    
    def __str__(self):
        return self.marque
    
