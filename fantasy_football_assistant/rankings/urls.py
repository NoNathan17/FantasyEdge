from django.urls import path
from . import views

urlpatterns = [
    path('', views.rankings_view, name='rankings'),
    path('quarterbacks/', views.quarterback_view, name='quarterback_rankings'),
    path('runningbacks/', views.runningback_view, name='runningback_rankings'),
    path('widerecievers/', views.widereceiver_view, name='widereciever_rankings'),
    path('tightends/', views.tightend_view, name='tightend_rankings'),
    path('kickers/', views.kicker_view, name='kicker_rankings'),
]