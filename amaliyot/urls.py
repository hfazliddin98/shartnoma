from django.urls import path
from .views import amaliyotlar, update_amaliyot

urlpatterns = [
    path('', amaliyotlar, name='amaliyot'),   
    path('update_amaliyot/<int:pk>/', update_amaliyot, name='update_amaliyot'),  
]
