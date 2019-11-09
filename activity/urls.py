"""activityurls.py page"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.activity, name="activity"),
    path('watched/', views.watched, name="activity"),
    path('watch/', views.watch, name="activity"),
    path('watchedlist/', views.watchedlist, name="activity"),
    path('watchlist/', views.watchlist, name="activity"),
    path('ajaxremovewatchlist/', views.ajaxremovewatchlist, name="ajaxremovewatchlist"),
    path('ajaxremovewatchedlist/', views.ajaxremovewatchedlist, name="ajaxremovewatchedlist"), #name kaam ka hai bc {% url '' %} ke liye
]
