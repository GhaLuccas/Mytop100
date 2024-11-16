from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Modelo Movie
class Movie(models.Model):
    title = models.CharField(max_length=80)
    director = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    score = models.IntegerField()

    def __str__(self):
        return self.title

# Modelo MovieList
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

# cria automaticamente uma MovieList ao registrar um usuário
@receiver(post_save, sender=User)
def create_movie_list_for_user(sender, instance, created, **kwargs):
    if created:  # Só cria quando um novo usuário é registrado
        MovieList.objects.create(user=instance)
