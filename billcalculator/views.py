from django.shortcuts import render
from django.http import HttpResponse
from .forms import Myform

# Create your views here.

def home(request):
	return render(request,'base.html',{'Form':Myform})

def expression(request):
  if request.method == 'POST':
    form = Myform(request.POST)
    if form.is_valid():
      units = int(form.cleaned_data['Unit'])
      rates = [3.80, 5.14, 5.36, 5.63, 8.70, 9.98]

      if units<=75:
      	total = units * rates[0]
      if 76 <= units <= 200:
      	total = 75 * rates[0] + (units-75) * rates[1]
      if 201 <= units <= 300:
      	total = 75 * rates[0] + 125 * rates[1] + (units-200) * rates [2]
      if 301 <= units <= 400:
      	total = 75 * rates[0] + 125 * rates[1] + 100 * rates [2] + (units-300) * rates[3]
      if 401 <= units <= 600:
      	total = 75 * rates[0] + 125 * rates[1] + 100 * rates [2] + 100 * rates[3] + (units-400)* rates[4]
      if units > 600:
      	total = 75 * rates[0] + 125 * rates[1] + 100 * rates [2] + 100 * rates[3] + 200 * rates[4] + (units-600) * 9.98

      return render(request, 'table.html', {'total':total, 'units':units})