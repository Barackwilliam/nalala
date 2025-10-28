#lodge_app/urls.py
from django.urls import path
from .views import home, book_room, dashboard, check_out, update_lodge
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('book/', book_room, name='book_room'),
    path('contact/', views.contact_view, name='contact'),
    path('dashboard/', dashboard, name='dashboard'),
    path('rooms/', views.room_list_view, name='room_list'),
    path('check_out/<int:guest_id>/', check_out, name='check_out'),
    path('update_lodge/', update_lodge, name='update_lodge'),
    path('Arusha_National_Park', views.Arusha_National_Park, name='Arusha_National_Park'),  # Add this line
    path('Kikuletwa_Hotsprings', views.Kikuletwa_Hotsprings, name='Kikuletwa_Hotsprings'),  # Add this line
    path('Tarangire_National', views.Tarangire_National, name='Tarangire_National'),  # Add this line
    path('Lake_Manyara_National', views.Lake_Manyara_National, name='Lake_Manyara_National'),  # Add this line
    path('condition', views.condition, name='condition'),  # Add this line
    path('policy', views.policy, name='policy'),  # Add this line
    path('Coffee_Tour', views.Coffee_Tour, name='Coffee_Tour'),  # Add this line
    path('abaut', views.abaut, name='abaut'),  # Add this line
    path('Ngorongoro_Crater', views.Ngorongoro_Crater, name='Ngorongoro_Crater'),  # Add this line
    path('login/', views.custom_login_view, name='custom_login'),  
    path('logout/', views.logout_view, name='logout'),
]