from django.db import models
from accounts.models import Customer

from core.models import PlasticWaste

class Conversation(models.Model):
    item = models.ForeignKey(PlasticWaste,related_name='conversations',on_delete=models.CASCADE)
    members = models.ManyToManyField(Customer,related_name='conversations')
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)

    

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation,related_name='messages',on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Customer,related_name='created_message',on_delete=models.CASCADE)
    readed = models.BooleanField(default=False)



