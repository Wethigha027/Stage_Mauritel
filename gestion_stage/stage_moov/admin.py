from django.contrib import admin
from .models import Utilisateur,Candidats,Service,Sujet_stage,Demandes,Document,Affectation,Evaluation,Attestation,Notification

# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Candidats)
admin.site.register(Demandes)
admin.site.register(Document)
admin.site.register(Service)
admin.site.register(Sujet_stage)
admin.site.register(Affectation)
admin.site.register(Attestation)
admin.site.register(Evaluation)
admin.site.register(Notification)