
from django.urls import path
from . import views

# TODO character generation to the front page
urlpatterns = [
    path('', views.character_page, name='character_page'),
    path('create_character/generate', views.generate_character,
         name='create_character'),

]
