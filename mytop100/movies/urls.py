from django.urls import path
from . import views  # Certifique-se de importar suas views

urlpatterns = [
    path("home/", views.home, name="home"),  # View de homepage
]
