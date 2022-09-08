from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from users.forms import CreationForm


# TODO function for signup.

def sign_up_view(request) -> HttpResponse:

    form = CreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')

    return render(request, 'registration/sign_up.html')


def login_view(request) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')

        else:  # Return an 'invalid login' error message.
            context = dict()
            context['error'] = 'Неправильный логин или пароль'
            return render(request, 'registration/login.html', context=context)

    else:
        return render(request, 'registration/login.html')
