from django.urls import path
import notion_updater.views as views

urlpatterns = [
    path('', views.test),
    path('meeting/<str:meeting_id>/', views.show_meeting, name='show_meetings'),
]