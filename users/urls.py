from django.urls import path
from .views import kirish, home, royhat, superadmin, dekanat, talabalar, adminlar
from .views import super_admin, dekanat_admin, shartnoma_olgan, dekanat_shartnoma_olgan
from .views import dekanat_talaba, talaba_qidiruv, talaba_ochirish



urlpatterns = [
    path('kirish/', kirish, name='kirish'),
    path('', home, name='home'),
    path('royhat/', royhat, name='royhat'),
    path('superadmin/', superadmin, name='superadmin'),
    path('dekanat/', dekanat, name='dekanat'),
    path('dekanat_admin/', dekanat_admin, name='dekanat_admin'),
    path('super_admin/', super_admin, name='super_admin'),
    path('talabalar/', talabalar, name='talabalar'),
    path('adminlar/', adminlar, name='adminlar'),
    path('shartnoma_olgan/', shartnoma_olgan, name='shartnoma_olgan'),
    path('dekanat_shartnoma_olgan/', dekanat_shartnoma_olgan, name='dekanat_shartnoma_olgan'),
    path('dekanat_talaba/', dekanat_talaba, name='dekanat_talaba'),
    path('talaba_qidiruv/', talaba_qidiruv, name='talaba_qidiruv'),
    path('talaba_ochirish/<int:pk>/', talaba_ochirish, name='talaba_ochirish'),
]