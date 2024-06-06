from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('success/', views.reservation_success, name='success'),
    path('submit_reservation/', views.submit_reservation, name='submit_reservation'),
    path('menu/', views.menu, name='menu'),
    path('menu_item/<int:pk>/', views.menu_item, name="menu_item"),
]