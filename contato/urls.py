from django.urls import path
from .views import homepage, excluirContato

app_name = 'contato'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('excluirContato/<int:contato_id>', excluirContato, name='excluirContato'),
]
