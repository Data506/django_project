from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def about_me(request):
    return render(request, 'myapp/about_me.html')