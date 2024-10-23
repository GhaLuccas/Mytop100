from . import views  
from django.urls import path

urlpatterns = [
    path("movies/", views.get_all_movies, name="get_all"),
    path("movie/<int:movie_id>/", views.get_one_movie, name="get_one"),
    path("create-movie/" , views.create_movie , name="ceate-movie"),
    path("remove-movie/<int:movie_id>/" , views.delete_movie, name="delete_movie") ,
    path("generic/movies/", views.GenericListAllAPI.as_view(), name="generic_all"),  
    path("generic/movie/<int:movie_id>/", views.GenericMovieRetrieveAPI.as_view(), name="generic_one"),
    path("generic/delete/<int:movie_id>/", views.GenericDeleteMovieAPI.as_view() , name="generic_del"),
]
