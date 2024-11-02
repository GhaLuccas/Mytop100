from django.urls import path
from . import views  

urlpatterns = [
    path("home/", views.home, name="home"),  
    path("list/", views.my_movie_list, name="list"),  
    path('movies/add/', views.add_movie, name='add_movie'),
    path('movies/remove/<int:movie_id>/', views.remove_movie, name='remove_movie'),
]
