from django.shortcuts import render, redirect
from .forms import UtilisateurForm,CandidateForm,ServiceForm
from .models import Utilisateur
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
#les views pour gestions des utilisateur
def create_utilisateur(request):
    if request.method == 'POST':
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hello')  # Replace 'success_url' with your desired redirect URL
    else:
        form = UtilisateurForm()
    
    return render(request, 'gestions_users/create_utilisateur.html', {'form': form})
def hello(request):
    return render(request,'gestions_users/hello.html',{'hello':'hello'})
def interface_principal(request):
    return render(request,'gestions_users/hello_user.html',{'home':'home'} )
def home(request):
    error_message = None  # Initialise la variable pour stocker les messages d'erreur

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if email and password:
        
            utilisateur = Utilisateur.objects.filter(Email=email).first()

            if utilisateur and utilisateur.check_password(password):
               
                return redirect('hello') 
            else:
                error_message = "Email ou mot de passe incorrect."
        else:
            error_message = "Veuillez remplir tous les champs."

    user = request.user
   
    utilisateur_exists = Utilisateur.objects.filter(Email=user.email).exists() if user.is_authenticated else False

    return render(request, 'gestions_users/home.html', {
        'user': user,
        'utilisateur_exists': utilisateur_exists,
        'error_message': error_message, 
    })

#les views pour les candidates
def create_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('#')  # Replace 'success_url' with your desired redirect URL
    else:
        form = CandidateForm()
    
    return render(request, 'gestions_candidate/create_candidate.html', {'form': form})


#les views pour la service
def create_service(request):
    if request.method=='POST':
        form=ServiceForm(request.POST)
        if form .is_valid():
            form.save()
            return redirect('#')
    else:
        form=ServiceForm()
    return render(request,'Service/ajouter_un_service.html',{'form':form})
# @login_required
# def admin_service_page(request):
#     # Vérifiez si l'utilisateur est admin
#     if request.user.role != 'admin':
#         return redirect('no_access')  # Rediriger si l'utilisateur n'est pas un admin

#     if request.method == 'POST':
#         service_form = ServiceForm(request.POST)
#         if service_form.is_valid():
#             service_form.save()
#             return redirect('admin_service_page')  # Rediriger après la création du service
#     else:
#         service_form = ServiceForm()

#     utilisateurs = Utilisateur.objects.all()

#     context = {
#         'service_form': service_form,
#         'utilisateurs': utilisateurs,
#     }
#     return render(request, 'admin_service_page.html', context)

