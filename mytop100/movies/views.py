from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie, MovieList

from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import MovieSerializer


# Create your views here.


def home(request):
  movies = Movie.objects.all()
  context = {
     'movies':movies
  }
  return render(request, "home.html", context)


# this fucn get the user movie list
@login_required
def my_movie_list(request):
    movie_list = get_object_or_404(MovieList, user=request.user)
    
    context = {
        'movie_list': movie_list,
        'movies': movie_list.movies.all(),  
    }
    
    return render(request, "movielist.html", context)


@login_required
def add_movie(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        movie = get_object_or_404(Movie, id=movie_id)
        movie_list, created = MovieList.objects.get_or_create(user=request.user)
        movie_list.add_movie(movie)
        return redirect('list')  

    
    movies = Movie.objects.all()
    return render(request, 'add_movie.html', {'movies': movies})
   
@login_required
def remove_movie(request, movie_id):
    movie_list = get_object_or_404(MovieList, user=request.user)
    movie = get_object_or_404(Movie, id=movie_id)
    
    try:
        movie_list.remove_movie(movie)
    except ValueError as e:
        print(e)
    return redirect('list') 