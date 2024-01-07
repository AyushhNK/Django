from django import forms

class CityName(forms.Form):
	city=forms.CharField(label="Name of city",max_length=20)