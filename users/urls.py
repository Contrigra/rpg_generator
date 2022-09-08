from django.urls import path

from users.views import sign_up_view, login_view

urlpatterns = [
    path('signup/', sign_up_view, name='sign_up'),
    path('login/', login_view, name='rpg_login')

]
