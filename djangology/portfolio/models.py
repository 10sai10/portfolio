
from django.db import models

class Actif(models.Model):
    ETAT_CHOICES = [
       ('Non détenu', 'Non détenu'),
       ('Acheté', 'Acheté'),
   ]
    
    nom = models.CharField(max_length=100)
    prix = models.FloatField()
    quantite_disponible = models.IntegerField(default=0)
    etat = models.CharField(max_length=20, choices=ETAT_CHOICES, default='Non détenu')
    lien_web = models.URLField()
    
class Transaction(models.Model):
    actif = models.ForeignKey(Actif, on_delete=models.CASCADE)
    type_transaction = models.CharField(max_length=10, choices=[('Achat', 'Achat'), ('Vente', 'Vente')])
    quantite = models.IntegerField()
    date_transaction = models.DateTimeField(auto_now_add=True)

class Portefeuille(models.Model):
    argent_disponible = models.FloatField(default=10000.0)