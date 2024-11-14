#Apis urls 
from . import views
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("movies/", views.MovieListCreateAPIView.as_view(), name="plural"),
    path("movies/<int:movie_id>/" , views.MovieRetrieveUpdateDestroyAPIView.as_view() ,name='singular'),
    path("movielist/" , views.MovieListApi.as_view() , name="movie-list") ,
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

