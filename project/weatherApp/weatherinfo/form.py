from django import forms

class CityName(forms.Form):
	city=forms.CharField(label="city name",max_length=20)