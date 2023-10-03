from django.db import models

# Create your models here.


class Flights(models.Model):
    Flight_no = models.CharField(max_length=20,primary_key=True, unique=True)
    Airline_name = models.CharField(max_length=50)
    no_of_seats = models.IntegerField()
    Base = models.CharField(max_length=50)
    Base_code = models.CharField(max_length=50)
    Destination = models.CharField(max_length=50)
    Destination_code = models.CharField(max_length=50)
    Arrival_time = models.DateTimeField(auto_now=True)
    Departure_time = models.DateTimeField(auto_now_add=True)
    Flight_price = models.IntegerField()

    def __str__(self):
        return f'{self.Airline_name} - {self.Flight_no} - {self.Base} - {self.Destination}'


class passengers(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    DOB = models.DateField()
    Gender = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254, unique=True)
    Phone_no = models.BigIntegerField()
    Nationality = models.CharField(max_length=30)
    Flight_no = models.ForeignKey(Flights, on_delete=models.CASCADE)
    Flight_from = models.CharField(max_length=50)
    Flight_to = models.CharField(max_length=50)

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.First_name} - {self.Nationality} - {self.Flight_from} - {self.Flight_to}'
