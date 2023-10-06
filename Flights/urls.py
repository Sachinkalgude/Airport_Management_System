from django.urls import path
from .views import show_flights_fields, flight_show, search_Flights


urlpatterns = [
    # path('passenger_data/', passenger_data, name='home'),
    # path('update/<int:id>/', passenger_data_update, name='update'),
    # path('delete/<int:id>/', Delete, name='delete'),
    # testing
    path('', show_flights_fields, name='main'),
    path('all_flights/', flight_show, name='show_db_Flights'),
    path('search_flights/', search_Flights, name='search')
]
