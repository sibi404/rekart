from django.forms import ModelForm
from django import forms

from accounts.models import Customer

from core.models import Products
from core.models import ProductCategory


CLASS_INPUT = 'block w-full rounded-md border-0 p-3 mb-4 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-500 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-primary sm:text-sm sm:leading-6'

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name','description','stock','price','image','category']

    name = forms.CharField(label='Name',widget=forms.TextInput(attrs={
        'name' : 'name',
        'class' : CLASS_INPUT
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'name' : 'description',
        'class' : CLASS_INPUT
    }))

    stock = forms.IntegerField(widget=forms.NumberInput(attrs={
        'name' : 'stock',
        'class' : CLASS_INPUT
    }))

    price = forms.DecimalField(widget=forms.NumberInput(attrs={
        'name' : 'price',
        'class' : CLASS_INPUT
    }))

    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'name' : 'image',
        'class' : CLASS_INPUT
    }))

    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(),widget=forms.Select(attrs={
        'name' : 'category',
        'class' : CLASS_INPUT
    }))