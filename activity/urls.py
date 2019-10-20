"""activityurls.py page"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.activity, name="activity"),
    path('watched/', views.watched, name="activity"),
    path('watch/', views.watch, name="activity"),
    path('addtowatched/', views.addtowatched, name="addtowatched"),
    path('addtowatch/', views.addtowatch, name="addtowatch"),
    path('removefromwatched/', views.removefromwatched, name="removefromwatched"),
    path('removefromwatch/', views.removefromwatch, name="removefromwatch"),
]
