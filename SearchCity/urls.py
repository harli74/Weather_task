from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('generate/',views.generateTab),
    path('search/',views.searchTAb)
]
