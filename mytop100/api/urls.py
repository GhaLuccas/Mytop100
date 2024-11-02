from . import views
from django.urls import path


urlpatterns = [
    path("movies/", views.MovieListCreateAPIView.as_view(), name="plural"),
    path("movies/<int:movie_id>/" , views.MovieRetrieveUpdateDestroyAPIView.as_view() ,name='singular'),
    path("movielist/" , views.MovieListApi.as_view() , name="movie-list")
]
