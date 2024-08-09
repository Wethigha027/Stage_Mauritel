from django import forms
from .models import Utilisateur,Candidats,Service
from django.contrib.auth.hashers import make_password

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['Nom_complet', 'Email', 'password', 'role']

        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
       
        utilisateur = super().save(commit=False)
        utilisateur.password = make_password(self.cleaned_data['password'])
        if commit:
            utilisateur.save()
        return utilisateur

#formulaire pour la candidate
class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidats
        fields = ['Nom_complet', 'universite', 'niveau_academique','specialite','Date_Naissance','email', 'telephone', 'cv', 'lettre_motivation', 'demande','periode']

    def save(self, commit=True):
        
        candidate = super().save(commit=False)
        
        if commit:
            candidate.save()

        return candidate
class AdminCandidateForm(forms.ModelForm):
    class Meta:
        model = Candidats
        fields = ['Id_utilisateur', 'Nom_complet', 'universite', 'niveau_academique','specialite','Date_Naissance','email', 'telephone','cv','lettre_motivation','demande','periode']  
#formulaire pour ajouter une service
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['Nom_service', 'description']
    
    def save(self, commit=True):
        
        service = super().save(commit=False)
        
        if commit:
            service.save()
        return service