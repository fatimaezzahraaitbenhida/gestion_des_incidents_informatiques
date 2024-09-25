from django.contrib import admin
from .models import *

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'email', 'mot_de_passe', 'service')

admin.site.register(Role)
admin.site.register(Type)
admin.site.register(Incident)
admin.site.register(employe)