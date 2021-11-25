
from django.urls import path
from . import views

urlpatterns = [
    path('create_character/', views.character_page, name='character_page'),
    path('create_character/generate', views.generate_character,
         name='create_character'),

]
