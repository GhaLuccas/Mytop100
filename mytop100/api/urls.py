from . import views  
from django.urls import path




#APP API paths 
urlpatterns = [
    path("movies/", views.get_all_movies, name="get_all"),  # Sem "movies/"
    path("movie/<int:movie_id>/", views.get_one_movie, name="get_one"),
    path("generic/movies/", views.GenericListAllAPI.as_view(), name="generic_all"),
    path("generic/movie/<int:pk>/", views.GenericDetailAPI.as_view(), name="generic_one"),
]
