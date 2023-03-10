from django.urls import path
from .views import kirish, home, royhat

urlpatterns = [
    path('', kirish, name='login'),
    path('home/', home, name='home'),
    path('signup/', royhat, name='signup'),
]