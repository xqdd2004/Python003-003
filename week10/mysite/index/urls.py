from django.urls import path, re_path, register_converter
from . import views

app_name = "index"

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.my_login, name='login')
]