from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from accounts.forms import RegistrationForm
from accounts.forms import User


def profile(request):
    return render(request, 'profile.html')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


class UserListGenericView(ListView):
    model = User
    template_name = 'accounts/index.html'
    context_object_name = 'users'


class UpdateUserGenericView(UpdateView):
    model = User
    form_class = RegistrationForm
    template_name = 'accounts/edit.html'
    success_url = '../index'
