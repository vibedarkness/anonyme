from django.shortcuts import render

from decimal import Decimal
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from .forms import TransForm, ClientForm
from .models import Transactions, Client
from django.db import transaction

# Create your views here.

from django.views import View


class IndexView(View):

    template_name="index.html"

    client=Client.objects.all()

    context={
        'client': client,
    }
        
    def get(self,request, *args, **kwargs):
        return render(request,self.template_name, self.context)
    
    def post(self,request, *args, **kwargs):
        return render(request,self.template_name)
    
    


class TransactionView(View):
    template_name="trans.html"
    
    def get(self,request, *args, **kwargs):
        form = TransForm()
        return render(request,self.template_name,{'form': form})
    
    def post(self,request, *args, **kwargs):
        form = TransForm()
        if request.method == 'POST':
            form = TransForm(data=request.POST)
            if form.is_valid():
                a = form.cleaned_data.get('nom')
                b = form.cleaned_data.get('recepteur')
                c = Decimal(form.cleaned_data.get('montant'))
                with transaction.atomic():
                    sender = Transactions.objects.get(nom=a)
                    sender.montant -=c
                    sender.save()
                    
                    recepteur = Transactions.objects.get(nom=b)
                    recepteur.montant += c 
                    recepteur.save()

                return HttpResponseRedirect('/')
            else:
                form = TransForm()

        return render(request, 'trans.html', {'form': form})
    



class ClientView(View):
    template_name="client.html"
    
    def get(self,request, *args, **kwargs):
        form = ClientForm()
        return render(request,self.template_name,{'form': form})
    
    def post(self,request, *args, **kwargs):
        form = ClientForm()
        if request.method == 'POST':
            form = ClientForm(data=request.POST)
            if form.is_valid():
                
                form.save()

                return HttpResponseRedirect('/')
            else:
                form = ClientForm()

        return render(request, 'trans.html', {'form': form})

