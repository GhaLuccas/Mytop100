from rest_framework import serializers
from .models import Movie , MovieList



class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'  


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MovieList
        fields = "__all__"