from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm 
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from .models import Service
from .form import SignupForm, LoginForm
from django.core.mail import send_mail
from .form import ContactForm
from .models import ContactSubmission

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})

@login_required
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'service_detail.html', {'service': service})

def aboutus(request):
    return render(request,'about.html')
    
def gallery(request):
    return render(request, 'gallery.html')


#  contactus
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            contact_submission = ContactSubmission(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                event_name=form.cleaned_data['event_name'],
                event_place=form.cleaned_data['event_place'],
                event_time=form.cleaned_data['event_time'],
                description=form.cleaned_data['description'],
            )
            contact_submission.save()

            # Send an email notification to the client
            send_mail(
                'New Event Booking Confirmation',
                f'Dear {contact_submission.name},\n\n'
                f'Thank you for booking your {contact_submission.event_name} event with us! Here are your event details:\n\n'
                f'Name: {contact_submission.name}\n'
                f'Email: {contact_submission.email}\n'
                f'Phone: {contact_submission.phone_number}\n'
                f'Event: {contact_submission.event_name}\n'
                f'Place: {contact_submission.event_place}\n'
                f'Time: {contact_submission.event_time}\n'
                f'Description: {contact_submission.description}\n\n'
                'We look forward to making your event special.\n\n'
                'Best Regards,\n'
                'Heliography Team',
                'your_email@gmail.com',  # Replace with your email
                [contact_submission.email],  # Client's email
                fail_silently=False,
            )

            # Redirect to a success page
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})