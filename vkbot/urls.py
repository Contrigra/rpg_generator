from django.urls import path
from . import views

urlpatterns = [
    path('', views.vk_view,
         name='vk_view'),

]
