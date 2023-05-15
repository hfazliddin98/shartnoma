from django.urls import path
from .views import kirish, home, royhat, superadmin, dekanat

urlpatterns = [
    path('kirish/', kirish, name='kirish'),
    path('', home, name='home'),
    path('royhat/', royhat, name='royhat'),
    path('superadmin/', superadmin, name='superadmin'),
    path('dekanat/', dekanat, name='dekanat'),
]