from django.shortcuts import render
from .models import Story, Bar


# Create your views here.
def index(request):
    stories = Story.objects.all().order_by('-created')[:3]
    bar = Bar.objects.all()[:1]

    context = {
        'stories': stories,
        'animate': True,
        'bars': bar
    }
    print(stories)

    return render(request, 'pages/index.html', context=context)


def council(request):
    return render(request, 'pages/council.html')


def events(request):
    return render(request, 'pages/events.html')

def contact(request):
    return render (request, 'pages/contact.html')