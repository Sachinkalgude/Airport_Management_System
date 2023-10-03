from django import forms
from .models import Flights, passengers


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
