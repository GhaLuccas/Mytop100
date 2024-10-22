from django.urls import path
from . import views  # Certifique-se de importar suas views

#APP Movies path
urlpatterns = [
    path("home/", views.home, name="home"),  # View de homepage
]
