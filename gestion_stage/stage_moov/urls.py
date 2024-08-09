from django.urls import path
from . import views
urlpatterns=[
    path('start_user',views.create_utilisateur, name='create_utilisateur'),
    path('hello',views.hello, name='hello'),
    path('',views.home, name='home'),
    path('interface',views.interface_principal, name='interface_principal'),
    path('create_candidate',views.create_candidate, name='create_candidate'),
    path('create_service',views.create_service, name='create_service'),
    ]