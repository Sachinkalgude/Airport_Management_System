from django.contrib import admin
from .models import Flights, passengers
# Register your models here.


@admin.register(Flights)
class FlightsAdmin(admin.ModelAdmin):
    list_display = ['Airline_name', 'no_of_seats', 'Flight_no',
                    'Arrival_time', 'Departure_time', 'Flight_price']


@admin.register(passengers)
class PassengersAdmin(admin.ModelAdmin):
    list_display = ['First_name', 'Gender', 'Nationality',
                    'Flight_no', 'Flight_from', 'Flight_to']
