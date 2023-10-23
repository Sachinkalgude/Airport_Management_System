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
    main_page,
    add_flight,
    show_flight,
    flight_update,
    delete_flight,
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
    #main page
    path('home_page/',main_page,name="HOME"),
    #add flight
    path('add_flight/',add_flight,name="add_flight"),
    #show flight
    path('flights/',show_flight,name="show_all_flights"),
    # flight update
    path('<int:Flight_no>/',flight_update,name='flight_update'),
    # flight delete
    path('flight_delete/<int:Flight_no>/',delete_flight,name='delete_flight'),
]
