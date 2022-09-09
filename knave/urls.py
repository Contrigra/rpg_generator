from django.urls import path
from . import views

# TODO character generation to the front page
urlpatterns = [
    path('character/generate/', views.generate_character,
         name='create_character'),

]
