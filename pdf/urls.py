from django.urls import path
from .views import pdf

urlpatterns = [
    path('', pdf, name='pdf'),
    # path('malumot_csv/', malumot_csv, name='malumot_csv'),     
]
