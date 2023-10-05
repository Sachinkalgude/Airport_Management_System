from django.urls import path
from .views import passenger_data, passenger_data_update, Delete, show_flights_fields


urlpatterns = [
    path('', passenger_data, name='home'),
    path('update/<int:id>/', passenger_data_update, name='update'),
    path('delete/<int:id>/', Delete, name='delete'),
    # testing
    path('index/', show_flights_fields),
]
