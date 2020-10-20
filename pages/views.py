from django.shortcuts import render
from .models import Story


# Create your views here.
def index(request):
    try:
        stories = Story.objects.all().order_by('-created')
        stories = stories[:3]
    except Exception:
        stories = []
    return render(request, 'pages/index.html', {'stories': stories, 'animate' : True})


def council(request):
    return render(request, 'pages/council.html')


def events(request):
    return render(request, 'pages/events.html')
