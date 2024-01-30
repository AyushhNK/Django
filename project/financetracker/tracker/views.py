from django.shortcuts import render
from .models import Transaction

# Create your views here.
def ChartView(request):
	transaction=Transaction.objects.all()
	label=[]
	data=[]
	for t in transaction: 
		label.append(t.description)
		data.append(t.amount)

	numeric_data=[]
	for d in data:
		numeric_data.append(float(d))


	return render(request,"chart.html",{"label":label,"data":numeric_data})
