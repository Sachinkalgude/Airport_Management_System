from django.shortcuts import render, redirect
from .forms import show_passengers_data
from .models import passengers
from django.http import HttpResponseRedirect
# Create your views here.


# def passenger_data(request):
#     p_data = passengers.objects.all()
#     p_forms = show_passengers_data()
#     if request.method == 'POST':
#         forms_data = show_passengers_data(request.POST)
#         if forms_data.is_valid():
#             # model_=passengers.objects.get(pk=id)
#             forms_data.save()
#             p_forms = show_passengers_data()
#     else:
#         p_forms = show_passengers_data()
#     return render(request, 'base.html', context={'pdata': p_data, 'pforms': p_forms})


# def passenger_data_update(request, id):
#     if request.method == 'POST':
#         model_ = passengers.objects.get(pk=id)
#         p_forms = show_passengers_data(request.POST, instance=model_)
#         if p_forms.is_valid():
#             p_forms.save()
#             # p_forms = show_passengers_data()
#         return redirect('home')
#     else:
#         model_ = passengers.objects.get(pk=id)
#         # p_forms = show_passengers_data()
#         p_forms = show_passengers_data(instance=model_)
#     return render(request, 'update.html', context={'pforms': p_forms})


# def Delete(request, id):
#     if request.method == 'POST':
#         model_ = passengers.objects.get(pk=id)
#         model_.save()
#         model_.delete()
#         return redirect('home')
