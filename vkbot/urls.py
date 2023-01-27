from django.urls import path
from . import views

urlpatterns = [
    path('server_confirm/', views.server_confirm,
         name='server_confirm'),

]
