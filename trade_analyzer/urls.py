# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('trade_analyzer/', views.trade_analyzer_view, name='trade_analyzer'),
]
