from django.shortcuts import render
from .models import Story, Bar


# Create your views here.
def index(request):
    try:
        stories = Story.objects.all().order_by('-created')
        bar = Bar.objects.all()[0]
        stories = stories[:3]
    except Exception:
        stories = []
        bar = None

    context = {
        'stories': stories,
        'animate': True,
        'bar': bar
    }

    return render(request, 'pages/index.html', context)


def council(request):
    return render(request, 'pages/council.html')


def events(request):
    return render(request, 'pages/events.html')

def contact(request):
    return render (request, 'pages/contact.html')