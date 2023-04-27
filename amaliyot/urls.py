from django.urls import path
from .views import amaliyot

urlpatterns = [
    path('', amaliyot, name='amaliyot'),     
]
