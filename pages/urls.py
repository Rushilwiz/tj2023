from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('council/', views.council, name='council'),
    path('events/', views.events, name='events')
]
