from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request , "congrats your account has been created")
            return redirect('movies:home')
        else:
            messages.error(request , "you did sofing wrong :()")
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

