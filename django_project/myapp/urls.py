from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-me/', views.about_me, name='about_me'),
        # Page where the user enters email
    path('subscribe/', views.subscribe_view, name='subscribe'),

    # Page shown after successful subscription
    path('subscribe/success/', views.subscribe_success_view, name='subscribe_success'),
]