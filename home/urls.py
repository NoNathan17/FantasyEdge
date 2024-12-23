from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('comingsoon/', views.coming_soon_view, name='live'),
]