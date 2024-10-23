from movies.models import Movie, MovieList

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from movies.serializers import MovieSerializer

from rest_framework import generics
from rest_framework.generics import RetrieveAPIView


@api_view(["GET"])
def get_all_movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_one_movie(request, movie_id):
    movie = get_object_or_404(Movie, id= movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)


def delete_movie(request , movie_id):
    movie = get_object_or_404(Movie , id=movie_id)
    if movie:
        movie.delete()
        return Response(status)


# Generics views


class GenericListAllAPI(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    
class GenericMovieRetrieveAPI(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class GenericDeleteMovieAPI(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer