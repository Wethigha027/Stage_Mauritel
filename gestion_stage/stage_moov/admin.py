from django.contrib import admin
from .models import Utilisateur,Candidats,Demandes,Document,Service,Sujet_stage,Affectation,Evaluation,Attestation,Notification
from .forms import UtilisateurForm,CandidateForm,AdminCandidateForm,ServiceForm
# Register your models here.
class UtilisateurAdmin(admin.ModelAdmin):
    form = UtilisateurForm 
    list_display = ('Nom_complet', 'Email','password' ,'role', 'Date_creation') 
# un class pour la chmaps specifique a l'interface de l'admin
class CandidatsAdmin(admin.ModelAdmin):
    form=AdminCandidateForm
    list_display=('Id_candidat','Nom_complet', 'universite', 'niveau_academique','Date_Naissance','email', 'telephone', 'cv', 'lettre_motivation', 'demande','periode','Date_demande')
#utilisation de formulaire personalliser
class ServiceAdmin(admin.ModelAdmin):
    form=ServiceForm
    list_display=['Id_service','Nom_service','description']
      
admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(Candidats,CandidatsAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Sujet_stage)
admin.site.register(Demandes)
admin.site.register(Document)
admin.site.register(Affectation)
admin.site.register(Evaluation)
admin.site.register(Attestation)
admin.site.register(Notification)

