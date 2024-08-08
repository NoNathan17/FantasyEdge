# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('schedules/', views.schedule_view, name='team_schedules'),
]
