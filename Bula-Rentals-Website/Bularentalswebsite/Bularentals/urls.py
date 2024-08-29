from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"), 
    path('reservation',views.reservation, name="reservation"),
    path('about_us', views.about_us, name="about_us"),
    path('fleet', views.fleet, name="fleet"),
    path('My_booking', views.My_booking, name="My_booking"),
    path('contact_us', views.contact_us, name="contact_us") 
]