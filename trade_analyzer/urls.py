# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('trade_analyzer/', views.trade_analyzer_view, name='trade_analyzer'),
    path('compare/', views.compare_trade, name='compare_trade'),
    path('autocomplete/', views.player_autocomplete, name='player_autocomplete')
]
