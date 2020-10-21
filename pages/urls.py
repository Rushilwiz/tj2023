from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name='contact'),
    path('council/', views.council, name='council'),
    path('events/', views.events, name='events'),
]
