from django.urls import path
from .views import kirish, home, royhat, superadmin, dekanat, talabalar, adminlar
from .views import super_admin, dekanat_admin

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
]