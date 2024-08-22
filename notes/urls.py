from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.notes_view, name='notes'),
    path('notes/<int:pk>', views.note_detail, name='note_detail'),
    path('notes/new', views.note_create, name='note_create'),
    path('notes/<int:pk>/delete', views.note_delete, name='note_delete'),
    path('notes/<int:pk>/edit', views.note_edit, name='note_edit'),

]
