from django.db import models
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.base import ContentFile
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

# def get_upload_path(instance, filename):
#     return f'Documents/documents_user_{instance.Id_candidat}/{filename}'

class Utilisateur(models.Model):
    Id_utilisateur = models.AutoField(primary_key=True)
    Nom_complet = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=100)
    Date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nom_complet
    # pour cacher password avant de save
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    

class Candidats(models.Model):
    Id_candidat = models.AutoField(primary_key=True)
    Id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True, blank=True)
    Nom_complet = models.CharField(max_length=150)
    universite = models.CharField(max_length=150)
    niveau_academique = models.CharField(max_length=150)
    specialite= models.CharField(max_length=150, default='TC')
    Date_Naissance = models.DateField()
    email = models.EmailField(max_length=254, unique=True)
    telephone = models.CharField(max_length=8, validators=[RegexValidator(regex=r'^[432]\d{7}$', message="Le numéro de téléphone doit être un numéro national")])
    Date_demande = models.DateTimeField(default=timezone.now)
    cv = models.FileField(upload_to='Documents/cv/',null=True,blank=True)
    lettre_motivation = models.FileField(upload_to='Documents/lettres_motivation/',null=True,blank=True)
    demande = models.FileField(upload_to='Documents/demandes/', null=False,blank=False)
    periode = models.CharField(max_length=100)

    def __str__(self):
        return self.Nom_complet
    


class Service(models.Model):
    Id_service = models.AutoField(primary_key=True)
    Nom_service = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)



    def __str__(self):
        return self.Nom_service

class Sujet_stage(models.Model):
    Id_sujet = models.AutoField(primary_key=True)
    Id_service = models.ForeignKey(Service, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    Description = models.TextField()
    Date_creation = models.DateTimeField(auto_now_add=True)
    Date_mise_a_jour = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

class Demandes(models.Model):
    Id_demande = models.AutoField(primary_key=True)
    Id_candidat = models.ForeignKey(Candidats, on_delete=models.CASCADE)
    Id_sujet = models.ForeignKey(Sujet_stage, on_delete=models.CASCADE)
    Date_soumission = models.DateTimeField()
    statut = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.Date_soumission is None:
            self.Date_soumission = self.Id_candidat.Date_demande
        super().save(*args, **kwargs)
    # pour id_demande=id_candidate
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.Id_demande:  
            self.Id_candidat = self.Id_demande
    def __str__(self):
        return str(self.Id_demande)

class Document(models.Model):
    Id_document = models.AutoField(primary_key=True)
    candidat = models.ForeignKey(Candidats, on_delete=models.CASCADE)
    Id_demande = models.ForeignKey(Demandes, on_delete=models.CASCADE)
    type_document = models.CharField(max_length=100, null=True, blank=True)
    chemin_document = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.candidat.Nom_complet}"

class Affectation(models.Model):
    Id_affectation = models.AutoField(primary_key=True)
    Id_demande = models.ForeignKey(Demandes, on_delete=models.CASCADE)
    Id_sujet = models.ForeignKey(Sujet_stage, on_delete=models.CASCADE)
    date_affectaion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Id_affectation)

class Evaluation(models.Model):
    Id_evaluation = models.AutoField(primary_key=True)
    Id_affectation = models.ForeignKey(Affectation, on_delete=models.CASCADE)
    Id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    Id_candidat = models.ForeignKey(Candidats, on_delete=models.CASCADE)
    commentaire = models.TextField()
    Note_performance = models.DecimalField(decimal_places=2, max_digits=10)
    date_evaluation = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Id_evaluation)

class Attestation(models.Model):
    Id_attestation = models.AutoField(primary_key=True)
    Id_affectation = models.ForeignKey(Affectation, on_delete=models.CASCADE)
    stagaire = models.ForeignKey(Candidats, on_delete=models.CASCADE)
    Date_emission = models.DateTimeField(auto_now_add=True)
    chemin_attestation = models.FileField(upload_to='Attestation/%y%m%d_{stagaire}')

    def __str__(self):
        return str(self.Id_attestation)

class Notification(models.Model):
    Id_notification = models.AutoField(primary_key=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    Message = models.TextField(max_length=255)
    Date_notification = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Id_notification)
