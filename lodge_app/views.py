# Updated core/views.py (or lodge_app/views.py - adjust based on your app name)
# Add import and compute total in dashboard view

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum  # Add this import
from .models import Lodge, Room, Guest, Payment
from .forms import GuestForm, PaymentForm, LodgeForm

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
