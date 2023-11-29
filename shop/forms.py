from django.forms import ModelForm
from django import forms

from accounts.models import Customer

from core.models import Products
from core.models import ProductCategory
from core.models import PlasticWaste
from core.models import Category

choice = PlasticWaste.UnitChoices


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



class PlasticWasteForm(ModelForm):
    class Meta:
        model = PlasticWaste
        fields = ['name','description','quantity','unit','price','category','image']
    
    name = forms.CharField(label='Name',widget=forms.TextInput(attrs={
        'name' : 'name',
        'class' : CLASS_INPUT
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'name' : 'description',
        'class' : CLASS_INPUT
    }))

    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'name' : 'quantity',
        'class' : CLASS_INPUT
    }))

    unit = forms.ChoiceField(choices=choice.choices,widget=forms.Select(attrs={
        'name' : 'unit',
        'class': CLASS_INPUT
    }))

    price = forms.DecimalField(widget=forms.NumberInput(attrs={
        'name' : 'price',
        'class' : CLASS_INPUT
    }))

    category = forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select(attrs={
        'name' : 'category',
        'class' : CLASS_INPUT
    }))

    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'name' : 'image',
        'class' : CLASS_INPUT
    }))