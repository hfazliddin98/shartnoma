from django.urls import path
from .views import pdf, malumot_csv, dekanat_csv, qoshimcha

urlpatterns = [
    path('shartnoma/<int:pk>/', pdf, name='pdf'),   
    path('malumot_csv/', malumot_csv, name='malumot_csv'), 
    path('dekanat_csv/', dekanat_csv, name='dekanat_csv'),

    # path('qoshimcha/', qoshimcha, name='qoshimcha'),
]
