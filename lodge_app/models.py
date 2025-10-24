from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField as UploadcareImageField  # Badilisha hapa

class Lodge(models.Model):
    name = models.CharField(max_length=255, default='Nalala House')
    location = models.CharField(max_length=255, default='Dar es Salaam, Tanzania')
    phone = models.CharField(max_length=20, default='0757179698')
    email = models.EmailField(default='aaron.ismail05@gmail.com')
    logo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name  # Sahihi, hakuna 'title'

    def get_og_image_url(self):
        return f"https://ucarecdn.com/{self.logo}/-/resize/1200x630/-/format/auto/"

    def get_image_url(self):
        return f"https://ucarecdn.com/{self.logo}/-/format/jpg/-/quality/smart/"


    class Meta:
        verbose_name = "Lodge"
        verbose_name_plural = "Lodges"
        ordering = ['name']




import logging

logger = logging.getLogger(__name__)

class Room(models.Model):
    lodge = models.ForeignKey('Lodge', on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=100)  # e.g., Nala, Simba
    room_type = models.CharField(max_length=50, default='Double')  # e.g., Single, Double, Suite
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, default=50.00)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Available', 'Available'),
            ('Booked', 'Booked'),
            ('Maintenance', 'Maintenance')
        ],
        default='Available'
    )
    image = models.CharField(max_length=255, blank=True, null=True)

    def get_og_image_url(self):
        return f"https://ucarecdn.com/{self.image}/-/resize/1200x630/-/format/auto/"

    def get_image_url(self):
        return f"https://ucarecdn.com/{self.image}/-/format/jpg/-/quality/smart/"




class Meta:
    verbose_name = "Room"
    verbose_name_plural = "Rooms"
    ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.lodge.name})"



class Guest(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    id_number = models.CharField(max_length=50)  # ID
    check_in = models.DateField()
    check_out = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Payment(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50, choices=[('Cash', 'Cash'), ('Bank', 'Bank')])
    paid_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.guest.name}"

class Staff(models.Model):
    role = models.CharField(max_length=100)  # e.g., Receptionist, Cook, Director
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.role