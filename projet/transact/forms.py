from django import forms

from . models import Transactions, Client

from django.core.validators import RegexValidator



class TransForm(forms.ModelForm):

   client = forms.CharField(required=False)
   recepteur = forms.CharField(max_length=1000)
   montant = forms.CharField(max_length=1000)
   class Meta:
        model = Transactions
        fields = "__all__"

        
class ClientForm(forms.ModelForm):

   prenom = forms.CharField(required=False)
   nom = forms.CharField(max_length=1000)
   adresse = forms.CharField(max_length=1000)
   somme = forms.CharField(max_length=1000)
   class Meta:
        model = Client
        fields = "__all__"