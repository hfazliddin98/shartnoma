from django.urls import path
from .views import pdf, malumot_csv, shartnoma

urlpatterns = [
    path('', pdf, name='pdf'),
    path('malumot_csv/', malumot_csv, name='malumot_csv'), 
    path('shartnoma/', shartnoma, name='shartnoma'),    
]
