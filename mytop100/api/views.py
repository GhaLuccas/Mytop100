from movies.models import Movie, MovieList
from movies.serializers import MovieSerializer
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView




# Class-Based Views (CBVs)
class MovieListCreateAPIView(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        movie = MovieSerializer(data=request.data)
        if movie.is_valid():
            movie.save()
            return Response(movie.data, status=status.HTTP_201_CREATED)
        else:
            return Response(movie.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieRetrieveUpdateDestroyAPIView(APIView):

    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, movie_id):
        updated_movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(updated_movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



