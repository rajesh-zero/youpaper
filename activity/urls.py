"""activityurls.py page"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.activity, name="activity"),
    path('watched/', views.watched, name="watched"),
    path('watch/', views.watch, name="watch"),
    path('watchedlist/', views.watchedlist, name="watchedlist"),
    path('watchlist/', views.watchlist, name="watchlist"),
    path('ajaxremovewatchlist/', views.ajaxremovewatchlist, name="ajaxremovewatchlist"),
    path('ajaxremovewatchedlist/', views.ajaxremovewatchedlist, name="ajaxremovewatchedlist"), #name kaam ka hai bc {% url '' %} ke liye
]
