from django.shortcuts import render
from .forms import ThingForm


def home(request):
    return render(request, 'home.html')

def things(request):
    form = ThingForm()
    return render(request, 'thing_sign_up.html' , {'form': form})
