from . import views  
from django.urls import path

urlpatterns = [
    # path("get_one/", views.get_all, name="get_all"), 
    path("all-movies/", views.get_all_movies, name="get_all"),
    path("one-movies/<int:movie_id>/", views.get_one_movie, name="get_one"),  
    path("generic/all-movies/", views.GenericListAllAPI.as_view(), name="get_all"),  
]
