from django.contrib import admin

from .models import *

# Register your models here.


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('client','montant')
    

class ClientAdmin(admin.ModelAdmin):
    list_display = ('prenom','nom','adresse','somme')

admin.site.register(Client, ClientAdmin)


admin.site.register(Transactions,TransactionAdmin)
