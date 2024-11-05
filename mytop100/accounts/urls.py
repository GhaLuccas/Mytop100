from django.contrib.auth import views as auth_views
from .views import registro
from django.urls import path

app_name = "accounts"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='movies:home'), name='logout'),
    path('registro/', registro, name='registro'),
]
