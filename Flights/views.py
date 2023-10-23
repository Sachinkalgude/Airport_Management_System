from django.shortcuts import render, redirect
from .forms import show_passengers_data, flights_form
from .models import passengers, Flights
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from Authentication_App.models import user
# Create your views here.


# on home page.
def show_flights_fields(request):
    fs = flights_form()
    return render(request, 'index.html', context={'fs': fs})

# on flights page all flights.


def flight_show(request):
    fg = Flights.objects.all()
    return render(request, 'flights.html', context={'fg': fg})

# search flights.
# to show available flights by searching.


def search_Flights(request):
    if request.method == 'GET':
        base = request.GET.get('Base')
        destination = request.GET.get('Destination')
        print(base)
        print(destination)
        return render(request,'search_flights.html',context={'base':base,'destination':destination})
    else:
        return redirect('home')


def passenger_data(request):
    p_data = passengers.objects.all()
    p_forms = show_passengers_data()
    if request.method == 'POST':
        forms_data = show_passengers_data(request.POST)
        if forms_data.is_valid():
            # model_=passengers.objects.get(pk=id)
            forms_data.save()
            p_forms = show_passengers_data()
    else:
        p_forms = show_passengers_data()
    return render(request, 'all_data.html', context={'pdata': p_data, 'pforms': p_forms})


def passenger_data_update(request, id):
    if request.method == 'POST':
        model_ = passengers.objects.get(pk=id)
        p_forms = show_passengers_data(request.POST, instance=model_)
        if p_forms.is_valid():
            p_forms.save()
            # p_forms = show_passengers_data()
        return redirect('home')
    else:
        model_ = passengers.objects.get(pk=id)
        # p_forms = show_passengers_data()
        p_forms = show_passengers_data(instance=model_)
    return render(request, 'update.html', context={'pforms': p_forms})


def Delete(request, id):
    if request.method == 'POST':
        model_ = passengers.objects.get(pk=id)
        model_.save()
        model_.delete()
        return redirect('home')

# business page render


def business_page(request):
    return render(request, 'business.html')

# service page render


def service_page(request):
    return render(request, 'service.html')
