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
=======
<<<<<<< HEAD
>>>>>>> f8ad595ec5659fdbb31b80d323d58a3dce5c5690
=======
>>>>>>> 8ff632ce1a1cb6fa89d4f695f037482237717b5b
>>>>>>> f8ad595ec5659fdbb31b80d323d58a3dce5c5690
    path('malumot_csv/', malumot_csv, name='malumot_csv'), 
    path('dekanat_csv/', dekanat_csv, name='dekanat_csv'),
]
