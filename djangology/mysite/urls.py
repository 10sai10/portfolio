from django.contrib import admin
from django.urls import path, include
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.liste_actifs, name='liste_actifs'),
    path('', include('portfolio.urls')),
]
