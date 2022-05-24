# -*- encoding: utf-8 -*-
from django import forms
from .models import Producto, Factura, Registro
from django.forms.models import inlineformset_factory

class FacturaForm(forms.ModelForm):
    class Meta():
        model = Factura
        #exclude = ['']

class RegistroForm(object):
    class Meta():
        model = Registro
        #exclude = 

RegistroFormSet = inlineformset_factory(Factura, Registro)