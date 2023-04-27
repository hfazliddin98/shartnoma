from django.urls import path
from .views import home, kirish
from .views import kirish, home, royhat

urlpatterns = [
    path('kirish/', kirish, name='kirish'),
    path('', home, name='home'),
    path('royhat/', royhat, name='royhat'),
]