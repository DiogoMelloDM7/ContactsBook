from django.urls import path
from .views import homepage

app_name = 'contato'

urlpatterns = [
    path('', homepage, name='homepage'),
    
]
