from django.contrib import admin
from django.db import models
from django import forms
from django.forms import widgets
from qlns.models import *
# Import our custom widget and our model from where they're defined
from .models import *
from qlns.models import *

class ThongbaoForm(forms.ModelForm):
    class Meta:
        model = Thongbao
        fields = "__all__"
        widgets={
            'tieude':forms.TextInput(attrs={'class':"form-control" })
        }
    
class QuyDinhcongtyForm(forms.ModelForm):
    class Meta:
        model = Quydinhcongty
        fields = "__all__"
        

class QuyDinhphongbanForm(forms.ModelForm):
    class Meta:
        model = Quydinhphongban
        fields = "__all__"


class QuyTrinhphongbanForm(forms.ModelForm):
    class Meta:
        model = Quytrinhphongban
        fields = "__all__"
        

class QuyTrinhcongtyForm(forms.ModelForm):
    class Meta:
        model = Quytrinhcongty
        fields = "__all__"
      

class ChedocongtyForm(forms.ModelForm):
    class Meta:
        model = Chedocongty
        fields = "__all__"

class ChedophongbanForm(forms.ModelForm):
    class Meta:
        model = Chedophongban
        fields = "__all__"




    