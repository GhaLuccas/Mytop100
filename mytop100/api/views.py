from movies.models import Movie, MovieList

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from movies.serializers import MovieSerializer

from rest_framework import generics
from rest_framework.generics import RetrieveAPIView , CreateAPIView


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


@api_view(["POST"])
def create_movie(request):
    movie = MovieSerializer(data=request.data)
    if movie.is_valid():
        movie.save()
        return Response(movie.data , status=status.HTTP_201_CREATED)
    return Response(movie.errors , status=status.HTTP_400_BAD_REQUEST)


@api_view(["UPDATE"])
def update_movie(request , movie_id):
    update_movie = get_object_or_404(Movie , movie_id)
    update_movie = MovieSerializer(data=request.data)
    if update_movie.is_valid():
        update_movie.save()
        return Response(update_movie.data , status=status.HTTP_201_CREATED)

@api_view(['DELETE']) 
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return Response({"message": f"Movie with id {movie_id} has been deleted successfully."}, 
                    status=status.HTTP_200_OK)


# Generics views


class GenericListAllAPI(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    
class GenericMovieRetrieveAPI(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class GenericCreateMovieAPI(generics.CreateAPIView):
    serializer_class = MovieSerializer
    
class GenericUpdateMovieAPI(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class GenericDeleteMovieAPI(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
