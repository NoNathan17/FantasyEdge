from django.urls import path
from . import views

urlpatterns = [
    path('', views.rankings_view, name='rankings'),
    path('rankings/quarterbacks/', views.quarterback_view, name='quarterback_rankings'),
    path('rankings/runningbacks/', views.runningback_view, name='runningback_rankings'),
    path('rankings/widerecievers/', views.widereciever_view, name='widereciever_rankings'),
    path('rankings/tightends/', views.tightend_view, name='tightend_rankings'),
    path('rankingskickers/', views.kicker_view, name='kicker_rankings'),
]