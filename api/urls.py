from . import views  
from django.urls import path

urlpatterns = [
    # path("get_one/", views.get_all, name="get_all"), 
    path("movies/", views.get_all_movies, name="get_all"),
    path("movie/<int:movie_id>/", views.get_one_movie, name="get_one"),  
    path("generic/movies/", views.GenericListAllAPI.as_view(), name="generic_all"),  
    path("generic/movie/<int:movie_id>/", views.GenericDetailAPI.as_view(), name="generic_one")
]
