from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.notes_view, name='notes'),
    path('notes/<int:pk>', views.notes_detail, name='notes_detail'),
    path('notes/new', views.note_create, name='note_create'),
]
