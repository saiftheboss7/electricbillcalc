from django import forms

class Myform(forms.Form):
    Unit = forms.CharField(
        label = "Enter your total unit",
        max_length = 80,
        required = True,
    )