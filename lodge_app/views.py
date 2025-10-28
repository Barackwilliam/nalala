# Updated core/views.py (or lodge_app/views.py - adjust based on your app name)
# Add import and compute total in dashboard view

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum  # Add this import
from .models import Lodge, Room, Guest, Payment
from .forms import GuestForm, PaymentForm, LodgeForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import ContactMessage

def home(request):
    lodge = Lodge.objects.first()
    rooms = Room.objects.all()
    return render(request, 'index.html', {'lodge': lodge, 'rooms': rooms})

def book_room(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            guest = form.save()
            guest.room.status = 'Booked'
            guest.room.save()
            return redirect('home')
    else:
        form = GuestForm()
    return render(request, 'booking.html', {'form': form})

@login_required
def dashboard(request):
    guests = Guest.objects.all()
    rooms = Room.objects.all()
    payments = Payment.objects.all()
    total_revenue = payments.aggregate(total=Sum('amount'))['total'] or 0  # Compute here
    return render(request, 'dashboard.html', {'guests': guests, 'rooms': rooms, 'payments': payments, 'total_revenue': total_revenue})

@login_required
def check_out(request, guest_id):
    guest = get_object_or_404(Guest, id=guest_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.guest = guest
            payment.save()
            guest.room.status = 'Available'
            guest.room.save()
            guest.delete()
            return redirect('dashboard')
    else:
        form = PaymentForm()
    return render(request, 'check_out.html', {'form': form, 'guest': guest})

@login_required
def update_lodge(request):
    lodge = Lodge.objects.first()
    if request.method == 'POST':
        form = LodgeForm(request.POST, request.FILES, instance=lodge)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = LodgeForm(instance=lodge)
    return render(request, 'update_lodge.html', {'form': form})


# core/views.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


from django.contrib.auth import logout as auth_logout
def logout_view(request):
    auth_logout(request)  # hii sasa ni ya Django halisi, siyo yako
    return redirect('/')



def Arusha_National_Park(request):
    return render(request,"Arusha_National.html")


def Kikuletwa_Hotsprings(request):
    return render(request,"Kikuletwa_Hotsprings.html")


def Tarangire_National(request):
    return render(request,"Tarangire_National.html")


def Lake_Manyara_National(request):
    return render(request,"Lake_Manyara_National.html")


def Coffee_Tour(request):
    return render(request,"Coffee_Tour.html")


def Ngorongoro_Crater(request):
    return render(request,"Ngorongoro_Crater.html")

def condition(request):
    return render(request,"condition.html")

def policy(request):
    return render(request,"policy.html")
def abaut(request):
    return render(request,"abaut.html")






def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the message to database
            contact_message = form.save()
            
            # Send email notification (optional)
            try:
                send_mail(
                    f'New Contact Message: {contact_message.subject}',
                    f'''
                    New message from {contact_message.name} ({contact_message.email})
                    Phone: {contact_message.phone or 'Not provided'}
                    
                    Message:
                    {contact_message.message}
                    ''',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.CONTACT_EMAIL],  # Add this to your settings
                    fail_silently=True,
                )
            except:
                pass  # Email sending is optional
            
            # Success message
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})




def room_list_view(request):
    """View kuonyesha rooms zote tu"""
    rooms = Room.objects.select_related('lodge').all()
    lodges = Lodge.objects.all()
    
    # Filter by lodge kama ipo katika request
    lodge_id = request.GET.get('lodge')
    if lodge_id:
        rooms = rooms.filter(lodge_id=lodge_id)
    
    context = {
        'rooms': rooms,
        'lodges': lodges,
        'selected_lodge': lodge_id
    }
    return render(request, 'room_list.html', context)