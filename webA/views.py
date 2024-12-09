from django.shortcuts import render

def home(request):
    return render(request, 'webA/home.html')

def about(request):
    return render(request, 'webA/about.html')

def densha(request):
    return render(request, 'webA/densha.html')

def works(request):
    return render(request, 'webA/web.html')

def games(request):
    return render(request, 'webA/games.html')





