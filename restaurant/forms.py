from django.forms import ModelForm
from .models import Reservation


# Code added for loading form data on the Booking page
class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'date', 'time']
