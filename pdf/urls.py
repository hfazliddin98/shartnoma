from django.urls import path
from .views import pdf, malumot_csv, dekanat_csv, qrcode

urlpatterns = [
    path('', pdf, name='pdf'),
    path('qrcode/<int:pk>/', qrcode, name='qrcode'),
    path('malumot_csv/', malumot_csv, name='malumot_csv'), 
    path('dekanat_csv/', dekanat_csv, name='dekanat_csv'),
]
