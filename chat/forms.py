from django import forms
from django.forms import ModelForm
from . models import ConversationMessage

class ConversationMessageForm(ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)

    content = forms.CharField(widget=forms.TextInput(attrs={
        'name' : 'message',
        'class' : 'h-10 w-full outline-none border-none rounded px-3 text-sm focus:ring-0',
        'placeholder' : 'Type your message...',
        'autocomplete' : 'off'
    }))
