from django.urls import path
from . import views

urlpatterns = [
    path('', views.meeting_overview, name='notes'),
    path('meeting/<str:meeting_id>/', views.show_meeting, name='show_meetings'),
]