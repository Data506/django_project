from django.shortcuts import render, redirect
from django.contrib import messages  # for error messages (optional)
from .models import Subscriber

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def about_me(request):
    return render(request, 'myapp/about_me.html')

def subscribe_view(request):

    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        if email:
            Subscriber.objects.create(email=email)
            return redirect('subscribe_success')
        else:
            # No email provided; show an error message or handle as needed
            messages.error(request, 'Please enter your email address.')

    return render(request, 'myapp/subscribe.html')

def subscribe_success_view(request):
    return render(request, 'myapp/subscribe_success.html')


