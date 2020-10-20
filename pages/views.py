from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pages/index.html', context={'animate': True})


def council(request):
    return render(request, 'pages/council.html')


def events(request):
    return render(request, 'pages/events.html')
