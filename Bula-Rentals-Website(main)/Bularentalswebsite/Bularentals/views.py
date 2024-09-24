from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse
from .models import Vehicles
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Contact

# Create your views here.

def home(request):
    return render(request, 'home/Home.html')

def reservation(request):
    return render(request, 'home/Reservation.html')

def about_us(request):
    return render(request, 'home/About_us.html')

def fleet(request):
    vehicles = Vehicles.objects.all()
    return render(request, 'home/fleet.html', {'vehicles': vehicles})

def My_booking(request):
    return render(request, 'home/Booking.html')

#Search Function
def vehicle_search(request):
    query = request.GET.get('q')  
    if query:
        vehicles = Vehicles.objects.filter(
            Q(brand__icontains=query)  |         # Search by brand
            Q(model__icontains=query)            # Search by model       
        )
    else:
        vehicles = Vehicles.objects.all() 

    context = {'vehicles': vehicles}
    return render(request, 'home/Vehicles_Search.html', context)

#contact us function
def contact_us(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        question = request.POST.get('question')

        # Save the form data to the Contact model
        contact = Contact(name=name, email=email, phone=phone, question=question)
        contact.save()

        # Redirect to success page after form submission
        return redirect('contact_success')

    return render(request, 'home/contact_us.html')

def contact_success(request):
    return render(request, 'contact_success.html')
