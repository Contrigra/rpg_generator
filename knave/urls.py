from django.urls import path
from . import views

urlpatterns = [
    path('character/generate/', views.generate_character,
         name='create_character'),

]
