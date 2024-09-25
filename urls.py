from django.urls import path
from login_app import views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns =  [
    path("", views.render_login, name="render_login"),
    path("perform_login", views.perform_login, name="perform_login"),
    path("perform_logout", views.perform_logout, name="perform_logout"),
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path('admin_dashboard/ajouter/', views.ajouter_view, name="ajouter"),
    path('employe/aj/', views.aj_view, name="aj"),
    path('admin_dashboard/afficher/', views.afficher_view, name="afficher"),
    path('employe_dashboard/consulter/', views.consulter_view, name="consulter"),
    path('ajouter/', views.add_employee, name='add_employee'),
     path('ajouter/confirmation_ajout/', views.confirmation_ajout, name='confirmation_ajout'),
     path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
     path('technicien_dashboard/', views.technicien_dashboard, name='technicien_dashboard'),
    #path('register',views.register,name='register'),
    path('profile',views.profile,name='profile'),
    path('declarer',views.declarer,name='declarer'),
    path('add_incident/', views.add_incident, name='add_incident'),
     path('employe_dashboard/', views.employe_dashboard, name='employe_dashboard'),
     path('consulter/', views.consulter_view, name="consulter"),
     path('tec/', views.tec_view, name="tec"),
      path('update_statut/<int:incident_id>/<str:selected_statut>/', views.update_statut, name='update_statut'),
      
]