from django.shortcuts import render
from .forms import ThingForm

def home(request):
    form = ThingForm()
    return render(request, 'thing_sign_up.html' , {'form': form})
