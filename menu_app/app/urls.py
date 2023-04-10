from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, {'name': 'Home'}, name=''),
    path('about/', views.base, {'name': 'About company'}, name='about'),
    path('rates/', views.base, {'name': 'Exchange rates'}, name='rates'),
    path('rates/rub-usd', views.base, {'name': 'Cross rates rub-usd'}, name='rates_rub-usd'),
    path('rates/rub-usd/expanded', views.base, {'name': 'Cross rates rub-usd expanded info'},
         name='rates_rub_usd_expanded'),
    path('rates/rub-aud', views.base, {'name': 'Cross rates rub-aud'}, name='rates_rub-aud'),
    path('rates/rub-aud/expanded', views.base, {'name': 'Cross rates rub-aud expanded info'},
         name='rates_rub_aud_expanded'),
]
