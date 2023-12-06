from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from core.models import PlasticWaste
from . models import Conversation
from . forms import ConversationMessageForm
from accounts.models import Customer

def new_conversation(request,plastic_id):
    plastic = PlasticWaste.objects.get(id = plastic_id)
    user = User.objects.get(username=request.user)
    sender = Customer.objects.get(user = user)
    seller = Customer.objects.get(user = plastic.seller) 

    if request.method == 'POST':

        conversation = Conversation.objects.filter(item = plastic).filter(members__in=[sender])
        if conversation:
            conversation = conversation[0]
        else:
            conversation = Conversation.objects.create(item = plastic)
            conversation.members.add(sender)
            conversation.members.add(seller)
        
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.conversation = conversation
            obj.created_by = sender
            obj.save()
            conversation.save()
            return redirect('chat:new',plastic_id = plastic_id)
            

    else:
        messages = None
        conversation = Conversation.objects.filter(members__in=[sender]).filter(item = plastic)
        if conversation:
            conversation = conversation[0]
            messages = conversation.messages.all()
        form = ConversationMessageForm()
        context = {
            'form' : form,
            'messages' : messages
        }
    return render(request,'chat/new.html',context)


def inbox(request):
    user = User.objects.get(username = request.user)
    seller = Customer.objects.get(user = user)
    conversations = Conversation.objects.filter(members__in = [seller])

    context = {
        'conversations' : conversations
    }

    return render(request,"chat/inbox.html",context)
