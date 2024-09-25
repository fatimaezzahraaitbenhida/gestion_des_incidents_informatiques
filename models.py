from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class employe(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    nom= models.CharField(max_length=50)
    prenom=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    service = models.CharField(max_length=100,null=True)
    role=models.CharField(max_length=100,null=True)
    date = models.DateField(null=True, default=timezone.now)

    def __str__(self):
        return self.user.username
class Role(models.Model):
    idrole = models.IntegerField(primary_key=True)
    libellerole = models.CharField(max_length=50)

    def __str__(self):
        return f"ROLE\nID: {self.idrole}\nLibellé: {self.libellerole}"
class CustomUser(models.Model):
    nom = models.CharField(max_length=70,null=True)
    prenom = models.CharField(max_length=70,null=True)
    email = models.CharField(max_length=70,null=True)
    mot_de_passe = models.CharField(max_length=100,null=True)
    service = models.CharField(max_length=100,null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
         return f"USER\nNom: {self.nom}\nPrénom: {self.prenom}\n Email: {self.email}\n  Mot de passe: {self.mot_de_passe}\n Service: {self.service}"
class Type(models.Model):
    idtype = models.AutoField(primary_key=True)
    nomtype = models.CharField(max_length=100)

    def __str__(self):
        return f"TYPE\nID: {self.idtype}\nNom: {self.nomtype}"
class Incident(models.Model):
    STATUT_CHOICES = (
        ('Nouveau', 'Nouveau'),
        ('En Cours de Traitement', 'En Cours de Traitement'),
        ('Résolu', 'Résolu'),
        # Ajoutez d'autres statuts ici
    )
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    dateDeclaration = models.DateField(null=True, default=timezone.now)
    detailsreponse = models.TextField(null=True)
    datereparation = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relation avec le modèle User
    type =models.CharField(max_length=100,null=True)  # Relation avec le modèle Type
    statut = models.CharField(max_length=100, choices=STATUT_CHOICES, default='Nouveau')  # Champ pour le statut
    def __str__(self):
        return f"INCIDENT\nID: {self.id}\nDescription: {self.description}\nDate de déclaration: {self.dateDeclaration}\nDétails de réponse: {self.detailsreponse}\nDate de réparation: {self.datereparation}\nStatut: {self.statut}"