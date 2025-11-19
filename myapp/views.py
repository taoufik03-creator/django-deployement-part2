from django.shortcuts import render

# Create your views here.

from .models import Car
from .forms import CarForm


def homeview(request):
    form=CarForm()
    cars=Car.objects.all()
    if request.method=="POST":
        form=CarForm(request.POST)
        if form.is_valid():
            form.save()
    context={
        "form":form,
        "cars":cars

    }
    return render(request,"car_list.html",context)

def car_details(request,car_id):
    car=Car.objects.get(car_id=car_id)
    context={
        "car":car
    }
    return render(request,"car_details.html",context)
