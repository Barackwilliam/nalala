#lodge_app/urls.py
from django.urls import path
from .views import home, book_room, dashboard, check_out, update_lodge
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('book/', book_room, name='book_room'),
    path('dashboard/', dashboard, name='dashboard'),
    path('check_out/<int:guest_id>/', check_out, name='check_out'),
    path('update_lodge/', update_lodge, name='update_lodge'),
    path('login/', views.custom_login_view, name='custom_login'),  # Add this line
    path('logout/', views.logout_view, name='logout'),
]