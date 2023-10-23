from django.urls import path
from .views import (
    passenger_data,
    passenger_data_update,
    Delete,
    show_flights_fields,
    flight_show,
    search_Flights,
    business_page,
    service_page,
)


urlpatterns = [
    path('passenger_data/', passenger_data, name='home'),
    path('update/<int:id>/', passenger_data_update, name='update'),
    path('delete/<int:id>/', Delete, name='delete'),
    path('', show_flights_fields, name='main'),
    # all flights
    path('all_flights/', flight_show, name='show_db_Flights'),
    # search page
    path('search_flights/', search_Flights, name='search'),
    # business page
    path('business_page/', business_page, name='businesspage'),
    # service page
    path('service_page/', service_page, name='servicepage'),
]
