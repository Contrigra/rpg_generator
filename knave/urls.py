
from django.urls import path, include
from . import views

urlpatterns = [
    path('create_character/', views.generate_character, name='create_character'),
]
