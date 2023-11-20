from django.urls import path
from . import views

urlpatterns = [
    path('actifs/', views.liste_actifs, name='liste_actifs'),
    path('actif/<int:actif_id>/', views.acheter_vendre, name='acheter_vendre'),
]
