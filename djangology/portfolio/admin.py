from django.contrib import admin
from .models import Actif, Transaction, Portefeuille
admin.site.register(Actif)
admin.site.register(Transaction)
admin.site.register(Portefeuille)
