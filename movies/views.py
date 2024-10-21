from django.shortcuts import render
from .models import Movie, MovieList

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MovieSerializer


# Create your views here.


def home(request):
  movies = Movie.objects.all()
  return render(request, "home.html", {"movies": movies})


