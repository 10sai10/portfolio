from django.shortcuts import render, get_object_or_404
from .models import Actif, Transaction, Portefeuille
from .forms import TransactionForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.db import transaction
#import requests
#from bs4 import BeautifulSoup


def liste_actifs(request):
    actifs = Actif.objects.all()
    transactions = Transaction.objects.order_by('-date_transaction')[:8]
    portefeuille = Portefeuille.objects.first()
    return render(request, 'portfolio/liste_actifs.html', {'actifs': actifs, 'transactions': transactions, 'portefeuille': portefeuille})

@transaction.atomic
def acheter_vendre(request, actif_id):
    actif = get_object_or_404(Actif, pk=actif_id)
 #   prix = extraire_prix(actif.lien_web)
    form = TransactionForm()
    portefeuille = Portefeuille.objects.first()

    if request.method == 'POST':
        form = TransactionForm(request.POST)

        if form.is_valid():
            quantite = form.cleaned_data['quantite']
            type_transaction = form.cleaned_data['type_transaction']
            prix_total = actif.prix * quantite

            if type_transaction == 'Achat':
                if portefeuille.argent_disponible >= prix_total:
                    actif.quantite_disponible += quantite
                    actif.etat = 'Acheté'
                    portefeuille.argent_disponible -= prix_total
                else:
                    messages.error(request, "Vous n'avez pas assez d'argent pour acheter cet actif.")

            elif type_transaction == 'Vente':
                if actif.quantite_disponible - quantite < 0:
                    messages.error(request, "Vous ne pouvez pas vendre plus que la quantité disponible.")
                    return HttpResponseRedirect(reverse('liste_actifs'))

                actif.quantite_disponible -= quantite
                portefeuille.argent_disponible += prix_total
                if actif.quantite_disponible == 0:
                    actif.etat = 'Non détenu'
                    
            actif.save()
            portefeuille.save()

            transaction = form.save(commit=False)
            transaction.actif = actif
            transaction.save()

            return HttpResponseRedirect(reverse('liste_actifs'))

    return render(request, 'portfolio/acheter_vendre.html', {'actif': actif, 'form': form, 'portefeuille': portefeuille})



# def extraire_prix(lien_web):
#     try:
#         response = requests.get(lien_web)
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         prix_element = soup.find('fin-streamer', {'class': 'Fw(b)', 'data-test': 'qsp-price'})

#         prix = prix_element.get('value') if prix_element else 0
        
#         return prix
#     except Exception as e:
#         print(f"Erreur lors de l'extraction du prix : {e}")
#         return 0
