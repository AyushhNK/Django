# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Message
from .forms import MessageForm

# def inbox(request):
#     received_messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
#     return render(request, 'inbox.html', {'received_messages': received_messages})

def send_message(request, recipient_username):
    recipient = User.objects.get(username=recipient_username)
    recipient_id=recipient.id
    sender=User.objects.get(username=request.user)
    sender_id=sender.id

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = recipient
            message.save()
            return redirect(f'/send_message/{recipient_username}')
    else:
        form = MessageForm()
    received_messages =Message.objects.filter(
        Q(sender=request.user, receiver_id=recipient_id) | Q(sender_id=recipient_id, receiver=request.user)
    ).order_by('timestamp')
    return render(request, 'inbox.html', {'form': form, 'recipient': recipient,'received_messages': received_messages})



def chatPage(request, *args, **kwargs):
	if not request.user.is_authenticated:
		return redirect("login-user")
	users=User.objects.exclude(username=request.user).all()
	return render(request, "room.html",{"users":users})
