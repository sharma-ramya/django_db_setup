from django.shortcuts import render

# Create your views here.
from .models import *

def home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movie/home.html', context)