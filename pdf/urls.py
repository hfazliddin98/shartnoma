from django.urls import path
from .views import pdf, malumot_csv, dekanat_csv

urlpatterns = [
    path('', pdf, name='pdf'),
    path('malumot_csv/', malumot_csv, name='malumot_csv'), 
    path('dekanat_csv/', dekanat_csv, name='dekanat_csv'),
]
