from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=80)
    director = models.CharField(max_length=80)
    description  = models.TextField(max_length=100)

    def __str__(self):
        return self.title


class MovieList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie, blank=True)

    def __str__(self):
        return f"Lista de filmes de {self.user.username}"

    def add_movie(self, movie):
        if self.movies.count() < 100:
            self.movies.add(movie)
        else:
            raise ValueError("Sua lista já está bem cheia")
        
    def remove_movie(self, movie):
        if movie in self.movies.all(): 
            self.movies.remove(movie)  
        else:
            raise ValueError("Este filme não está na lista")

    def __len__(self):
        return self.movies.count()
