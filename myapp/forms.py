from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model=Car
        exclude=["car_id"]
        labels={
            "registration":"Registration ",
            "make":"Make ",
            "model":"Model ",
            "price":"Price ",
            "registration_date":"Registration date "
        }
        widgets={
            "registration_date":forms.DateInput(attrs={
                "type":'date'
            })
        }
