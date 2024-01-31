from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Transaction
from django.db.models import Sum
from .forms import TransactionForm
from django.db.models.functions import TruncMonth
from datetime import datetime

# Create your views here.

@login_required
def ChartView(request):
	transaction=Transaction.objects.all()
	label=[]
	data=[]
	date=[]
	for t in transaction: 
		label.append(t.description)
		data.append(t.amount)
		date.append(t.date)

	numeric_data=[]
	for d in data:
		numeric_data.append(float(d))

	actual_date=[]
	for d in date:
		actual_date.append(d.strftime('%Y-%m-%d'))

	monthly_summary = Transaction.objects.annotate(month=TruncMonth('date')).values('month').annotate(total_amount=Sum('amount'))

	return render(request,"chart.html",{"label":label,"data":numeric_data,"date":actual_date,'monthly_summary': monthly_summary})


def TransactionFormView(request):
	if request.method=="POST":
		form=TransactionForm(request.POST)
		if form.is_valid():
			form=form.save(commit=False)
			form.date=datetime.now().date()
			form.save()
			return redirect("chart")
	else:
		form=TransactionForm()
	return render(request,"transactionform.html",{"form":form})

