from django.urls import path
from . import views

urlpatterns = [
    path('rankings/overall', views.rankings_view, name='overall_rankings'),
    path('rankings/quarterbacks/', views.quarterback_view, name='quarterback_rankings'),
    path('rankings/runningbacks/', views.runningback_view, name='runningback_rankings'),
    path('rankings/widerecievers/', views.widereciever_view, name='widereciever_rankings'),
    path('rankings/tightends/', views.tightend_view, name='tightend_rankings'),
    path('rankings/kickers/', views.kicker_view, name='kicker_rankings'),
    path('rankings/defenses/', views.defense_view, name='defense_rankings'),


]