from django.urls import path
from .views import amaliyotlar

urlpatterns = [
    path('', amaliyotlar, name='amaliyot'),     
]
