from django import forms
from django.forms import ModelForm, widgets
from django.forms.forms import Form
from django.forms.widgets import NumberInput
from .models import *

class Formtrinhky(forms.ModelForm):
   
    class Meta:
        model = Tkhd
        fields = ['username','nhanvien','tieude','file','ghichu','guiduyet','trangthaiduyet_tp','trangthaiduyet_at',]
        
        
