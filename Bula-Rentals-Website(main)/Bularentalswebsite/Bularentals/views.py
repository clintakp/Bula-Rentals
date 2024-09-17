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

def contact_us(request):
    return render(request, 'home/contact_us.html')

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
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        question = request.POST.get('question')

        # Prepare email
        subject = 'Contact Us Form Submission'
        message = render_to_string('contact_email_template.html', {
            'name': name,
            'email': email,
            'phone': phone,
            'question': question,
        })
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['iankumar52@gmail.com']

        email = EmailMessage(subject, message, email_from, recipient_list)
        email.content_subtype = 'html'
        email.send()

        return redirect('contact_success')  # Redirect to a success page or home page
    
    return render(request, 'home/contact_us.html')

def contact_success(request):
    return render(request, 'contact_success.html')

#Display Fleet
#def vehicle_list(request):
    #vehicles = Vehicles.objects.all()
    #return render(request, 'home/fleet.html', {'vehicles': vehicles})