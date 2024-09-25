from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render ,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from .forms import IncidentRegistration
from .forms import Incidenta
from .forms import Incidentaa
from .models import CustomUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django .contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse

def update_statut(request, incident_id, selected_statut):
    # Your logic to update the statut here, for example:
    incident = Incident.objects.get(id=incident_id)
    incident.statut = selected_statut
    incident.save()
    
    return JsonResponse({"message": "Statut updated successfully"})


# Create your views here.

def render_login(request):
    return render(request, "login.html")
def perform_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if not username or not password:
            messages.error(request, "Username and password fields cannot be empty ")
            return redirect("render_login")  # Rediriger vers la page de login
            
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            if user.is_superuser:  # Vérifier si l'utilisateur est un admin
                return redirect("admin_dashboard")
            elif user.groups.filter(name='technicien').exists():  # Vérifier si l'utilisateur appartient au groupe "Techniciens"
                return redirect("technicien_dashboard")  # Rediriger vers la page technicien.html
            else:
                return redirect("employe_dashboard")
        else:
            messages.error(request, "Username or Password is Invalid ")
            return redirect("render_login")  # Rediriger vers la page de login
    
    return render(request, "login.html")
# def perform_login(request):
#     if request.method != "POST":
#         return render(request, "login.html")
#     else:
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         if not username or not password:
#             messages.error(request, "Username and password fields cannot be empty")
#             return HttpResponseRedirect("/")

#         user = authenticate(username=username, password=password)

#         if user is not None:
#             login(request, user)
            
#             # Check the role of the user
#             if user.email == username:  # Assuming email is used as the username
#                 return HttpResponseRedirect(reverse("employe_dashboard"))
#             elif user.is_staff:  # Assuming staff accounts are admins
#                 return HttpResponseRedirect(reverse("admin_dashboard"))
#             else:
#                 messages.error(request, "Unknown user role")
#                 return HttpResponseRedirect("/")
#         else:
#             messages.error(request, "Username or Password is Invalid")
#             return HttpResponseRedirect("/")
@login_required(login_url='perform_login')
def employe_dashboard(request):
    # Vous pouvez ajouter ici la logique pour récupérer et afficher les informations spécifiques à l'employé
    return render(request, 'employe.html')

@login_required(login_url='perform_login')
def admin_dashboard(request):
    return render(request, "admin_dashboard.html")
def technicien_dashboard(request):
    return render(request, "technicien.html")
def perform_logout(request):
    logout(request)
    return HttpResponseRedirect("/")
# def add_show(request):
#     if request.method == 'POST':
#         fm = IncidentRegistration(request.POST)
#     else:
#         fm = IncidentRegistration(request.POST)

#     return render(request, 'admin_dashboard.html',{'form':fm})

@login_required(login_url='perform_login')
def ajouter_view(request):
    return render(request, 'base.html')
  # Assurez-vous que le chemin du modèle est correct
@login_required(login_url='perform_login')
def aj_view(request):
    return render(request, 'profile.html')
@login_required(login_url='perform_login')
def afficher_view(request):
    return render(request, 'afficheremp.html')
@login_required(login_url='perform_login')
def consulter_view(request):
    return render(request, 'consulter.html') 
@login_required(login_url='perform_login')
def add_employee(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        mot_de_passe = request.POST.get('password')
        service = request.POST.get('service')
        role = request.POST.get('role')

        # Créer un nouvel utilisateur
        user = User.objects.create(
            first_name=nom,
            last_name=prenom,
            email=email,
            username=email  # Utiliser l'email comme nom d'utilisateur pour l'instant
        )
        user.set_password(mot_de_passe)  # Définir le mot de passe

        user.save()  # Enregistrer l'utilisateur

        # Créer un nouvel employé lié à l'utilisateur
        employe_instance = employe(user=user, nom=nom, prenom=prenom, email=email, role=role,service=service)
        employe_instance.save()
        

    return render(request, 'register.html')
@login_required(login_url='perform_login')
def add_show(request):
    if request.method == 'POST':
       fm = IncidentRegistration(request.POST)
       if fm.is_valid():
           fm.save()
    else:
       fm = IncidentRegistration()
    return render(request, 'base.html',{'form':fm})
@login_required(login_url='perform_login')
def afficher_view(request):
    users = employe.objects.all()  # Récupérer tous les utilisateurs de la base de données
    context = {'users': users}  # Passer les utilisateurs au contexte du template
    return render(request, 'afficheremp.html', context)
@login_required(login_url='perform_login')
def consulter_view(request):
    user = request.user
    incidents = Incident.objects.filter(user=user)  # Récupérer les incidents de l'utilisateur connecté
    context = {'incidents': incidents}
    return render(request, 'consulter.html', context)
@login_required(login_url='perform_login')
def tec_view(request):
    incidents = Incident.objects.all()  # Récupérer tous les incidents
    context = {'incidents': incidents}
    return render(request, 'tecaff.html', context)
@login_required(login_url='perform_login')

def confirmation_ajout(request):
    # Votre logique pour afficher la page de confirmation d'ajout
    return render(request, 'ajouter/confirmation_ajout.html')
@login_required(login_url='perform_login')
def edit_user(request, user_id):
    user = get_object_or_404(employe, id=user_id)
    
    if request.method == 'POST':
        user.nom = request.POST.get('nom')
        user.prenom = request.POST.get('prenom')
        user.email = request.POST.get('email')
        user.mot_de_passe = request.POST.get('password')
        user.service = request.POST.get('service')
        user.save()
        return redirect('afficher_view')  # Rediriger vers la liste des utilisateurs après modification
    
    context = {'user': user}
    return render(request, 'edit_user.html', context)
def edit_statut(request, incident_id):
    incident = get_object_or_404(Incident, pk=incident_id)
    
    if request.method == 'POST':
        incident.nom = request.POST.get('nom')
        incident.prenom = request.POST.get('prenom')
        incident.email = request.POST.get('email')
        incident.mot_de_passe = request.POST.get('password')
        incident.service = request.POST.get('service')
        incident.save()
        return redirect('afficher_view')  # Rediriger vers la liste des utilisateurs après modification
    
    context = {'user': incident}
    return render(request, 'edit_user.html', context)
@login_required(login_url='perform_login')


def edit_incident(request, incident_id):
    incident = get_object_or_404(Incident, pk=incident_id)
    
    if request.method == 'POST':
        email = request.POST.get('email').strip()  # Remove whitespace
        try:
            user = User.objects.get(email=email)
            
            incident.user = user
            incident.description = request.POST.get('description')
            incident.dateDeclaration = request.POST.get('dateDeclaration')
            incident.type = request.POST.get('type')
            
            incident.save()
            return redirect('consulter')  # Redirect to the list of incidents after modification
        except User.DoesNotExist:
            # Handle the case where the user doesn't exist
            # You might want to add a message to inform the user about this
            pass
    
    context = {'incident': incident}
    return render(request, 'edit_incident.html', context)

@login_required(login_url='perform_login')
def delete_user(request, user_id):
    user = get_object_or_404(employe, id=user_id)
    
    if request.method == 'POST':
        user.delete()
        messages.success(request, f"L'utilisateur {user.nom} {user.prenom} a été supprimé avec succès.")
        return redirect('afficher_view')  # Rediriger vers la liste des utilisateurs après suppression
    
    context = {'user': user}
    return render(request, 'delete_user.html', context)


# def registration(request):
#     if request.method == 'POST':
#         nom = request.POST.get('nom')
#         prenom = request.POST.get('prenom')
#         email = request.POST.get('email')
#         mot_de_passe = request.POST.get('password')
#         """ service = request.POST.get('service')
#         role =request.POST.get('role') """
#         try:
#             user = User.objects.create_user(first_name=nom,last_name=prenom,username=email,password=mot_de_passe)
#             employe.objects.create(user = user,nom=nom)
#             error ="no"
#         except:
#             error ="yes"
#     return render(request,'register.html',locals())

#     return render(request,'register.html')




# def emp_login(request):
#     return render(request, "emp_login.html")
""" def emp_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user =authenticate (username=username,
                                password=password)
        if user:
            login(request,user)
        
        return  render(request,'index.html') """
@login_required(login_url='perform_login')
def profile(request):
    return render(request, "profile.html")
@login_required(login_url='perform_login')

def declarer(request):
    return render(request, "declaration.html")
@login_required(login_url='perform_login')

def consulter(request):
    return render(request, "consulter.html")

def tec(request):
    return render(request, "tecaff.html")

""" def soumettre_incident(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        description = request.POST.get('description')
        type_nom = request.POST.get('type')

        # En supposant que vous avez un modèle Type
        try:
            instance_type = Type.objects.get(type=type_nom)
        except Type.DoesNotExist:
            instance_type = None

        if email and description and instance_type:
            # Créer et sauvegarder l'instance d'incident
            nouvel_incident = Incident(
                description=description,
                dateDeclaration=timezone.now(),
                user=request.user,  # En supposant que l'utilisateur est authentifié
                type=instance_type,
            )
            nouvel_incident.save()

            return redirect('employe')  # Rediriger vers une page de succès

    return render(request, 'declaration.html')  # Renvoyer la page du formulaire pour les requêtes GET """
@login_required(login_url='perform_login')

def add_incident(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        description = request.POST.get('description')
        incident_type = request.POST.get('type')
        
        # Créez un nouvel objet Incident et enregistrez les données
        incident = Incident.objects.create(
            description=description,
            user=request.user,  # Utilisateur connecté
            type=incident_type  # Stockez directement le nom du type d'incident
        )
        # Vous pouvez ajouter d'autres champs si nécessaire
        
        #return redirect('incident_list')  # Redirigez vers une page de liste d'incidents

    return render(request, 'declaration.html')
@login_required(login_url='perform_login')

def delete_incident(request, incident_id):
    incident = get_object_or_404(Incident, pk=incident_id)

    if request.method == 'POST':
        incident.delete()
        return redirect('consulter')  # Redirige vers la liste des incidents ou une autre vue

    context = {'incident': incident}
    return render(request, 'delete_incident.html', context)
