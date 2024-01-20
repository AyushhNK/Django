from django.shortcuts import render, HttpResponse,redirect
from . import models


# Create your views here.


def home(request):
    return render(request, 'home.html')



def contact(request):
    #contact form database
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = models.Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
    return redirect(home)
       

