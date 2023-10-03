from django import forms
from .models import Flights, passengers


# flights...
class flights_form(forms.ModelForm):
    class Meta:
        model = Flights
        fields = ['Flight_no','Airline_name','no_of_seats','Base','Base_code',
                  'Destination','Destination_code','Arrival_time','Departure_time','Flights_price']
        
        widgets = {
            'Flight_no': forms.TextInput(attrs={'class':'form-control'}),
            'Airline_name' : forms.TextInput(attrs={'class':'form-control'}),
            'no_of_seats' : forms.IntegerField(attrs={'class':'form-control'}),
            'Base' : forms.TextInput(attrs={'class':'form-control'}),
            'Base_code' : forms.TextInput(attrs={'class':'form-control'}),
            'Destination' : forms.TextInput(attrs={'class':'form-control'}),
            'Destination_code' : forms.TextInput(attrs={'class':'form-control'}),
            'Arrival_time' : forms.DateTimeField(attrs={'class':'form-control'}),
            'Departure_time' : forms.DateTimeField(attrs={'class':'form-control'}),
            'Flights_price' : forms.DecimalField(decimal_places=2,attrs={'class':'form-control'})
        }

class show_passengers_data(forms.ModelForm):

    class Meta:
        model = passengers
        fields = ['First_name', 'Last_name', 'DOB', 'Gender', 'Email',
                  'Phone_no', 'Nationality', 'Flight_no', 'Flight_from', 'Flight_to']
        widgets = {
            'First_name': forms.TextInput(attrs={'class': 'form-control', }),
            'Last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'DOB': forms.TextInput(attrs={'class': 'form-control'}),
            'Gender': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'class': 'form-control'}),
            'Phone_no': forms.TextInput(attrs={'class': 'form-control'}),
            'Nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'Flight_no': forms.Select(attrs={'class': 'form-control'}),
            'Flight_from': forms.TextInput(attrs={'class': 'form-control'}),
            'Flight_to': forms.TextInput(attrs={'class': 'form-control'}),
        }
