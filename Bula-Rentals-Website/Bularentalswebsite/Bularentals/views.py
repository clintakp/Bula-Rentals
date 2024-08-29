from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/Home.html')

def reservation(request):
    return render(request, 'home/Reservation.html')

def about_us(request):
    return render(request, 'home/About_us.html')

def fleet(request):
    return render(request, 'home/fleet.html')

def My_booking(request):
    return render(request, 'home/Booking.html')

def contact_us(request):
    return render(request, 'home/contact_us.html')