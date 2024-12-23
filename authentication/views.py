from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def signup_view(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()
    return render(response, "signup.html", {"form": form})