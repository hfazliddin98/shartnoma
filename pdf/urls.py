from django.urls import path
from .views import pdf, malumot_csv, dekanat_csv, qrcode

urlpatterns = [
<<<<<<< HEAD
    path('', pdf, name='pdf'),    
    path('qrcode/', qrcode, name='qrcode'),
=======
    path('', pdf, name='pdf'),
    path('qrcode/<int:pk>/', qrcode, name='qrcode'),
<<<<<<< HEAD
>>>>>>> f8ad595ec5659fdbb31b80d323d58a3dce5c5690
=======
>>>>>>> f8ad595ec5659fdbb31b80d323d58a3dce5c5690
    path('malumot_csv/', malumot_csv, name='malumot_csv'), 
    path('dekanat_csv/', dekanat_csv, name='dekanat_csv'),
]
