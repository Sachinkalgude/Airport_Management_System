from django import forms
from .models import Flights, passengers


# flights...
class flights_form(forms.ModelForm):
    Flight_no = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    Airline_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    no_of_seats = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    Base = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-css-control', 'placeholder': 'From'}))
    Base_code = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    Destination = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-css-control', 'placeholder': 'To'}))
    Destination_code = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    Arrival_time = forms.DateTimeField(
        widget=forms.SelectDateWidget(attrs={'class': 'custom-css-control', 'placeholder': 'Return'}))
    Departure_time = forms.DateTimeField(
        widget=forms.SelectDateWidget(attrs={'class': 'custom-css-control', 'placeholder': 'Depart'}))
    Flight_price = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Flights
        fields = ['Flight_no', 'Airline_name', 'no_of_seats', 'Base', 'Base_code',
                  'Destination', 'Destination_code', 'Arrival_time', 'Departure_time', 'Flight_price']


class show_passengers_data(forms.ModelForm):

    class Meta:
        model = passengers
        fields = ['First_name', 'Last_name', 'DOB', 'Gender', 'Email',
                  'Phone_no', 'Nationality', 'Flight_no', 'Flight_from', 'Flight_to','booking_id']
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
            'booking_id' : forms.TextInput(attrs={'class':'form-control'}),
        }
