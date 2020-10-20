from django.urls import path
from . import views

urlpatterns = [
    path('', views.test),
    path('meeting/<str:meeting_id>/', views.show_meeting, name='show_meetings'),
]