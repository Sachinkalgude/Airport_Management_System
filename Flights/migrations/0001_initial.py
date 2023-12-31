# Generated by Django 4.2.5 on 2023-10-03 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('Flight_no', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('Airline_name', models.CharField(max_length=50)),
                ('no_of_seats', models.IntegerField()),
                ('Base', models.CharField(max_length=50)),
                ('Base_code', models.CharField(max_length=50)),
                ('Destination', models.CharField(max_length=50)),
                ('Destination_code', models.CharField(max_length=50)),
                ('Arrival_time', models.DateTimeField(auto_now=True)),
                ('Departure_time', models.DateTimeField(auto_now_add=True)),
                ('Flight_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='passengers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Phone_no', models.BigIntegerField()),
                ('Nationality', models.CharField(max_length=30)),
                ('Flight_from', models.CharField(max_length=50)),
                ('Flight_to', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('Flight_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Flights.flights')),
            ],
        ),
    ]
