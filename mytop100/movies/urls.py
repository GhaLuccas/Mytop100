from django.urls import path
from . import views  # Certifique-se de importar suas views

urlpatterns = [
    path("/hi/", views.hi, name="hi"),  # Por exemplo, uma view de homepag
]
