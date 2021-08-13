from django.http import request
from khachhang.models import Khachhanglon
from django import forms
# from .models import Nhanvien
from django.contrib import admin
from django.forms import widgets
from django.forms.widgets import CheckboxInput, FileInput
from qlns.models import *
from ckeditor.widgets import CKEditorWidget
from django.http.request import *

class Create_khang_hang_lon(forms.ModelForm):
    class Meta:
        model = Khachhanglon
        fields = '__all__'
        baogia = forms.BooleanField(widget=CheckboxInput(), required=False)
         
        widgets ={
            'hangmuc':forms.Select(attrs={'label':'','class':'form-control'}),
            
        }
        
    def __init__(self,*args, **kwargs):
        super(Create_khang_hang_lon, self).__init__(*args, **kwargs)


class Edit_khang_hang_lon(forms.ModelForm):
    class Meta:
        model = Khachhanglon
        fields = '__all__'
        widgets ={
            'hangmuc':forms.Select(attrs={'label':'','class':'form-control'}),
            }
        
    def __init__(self,*args, **kwargs):
        super(Edit_khang_hang_lon, self).__init__(*args, **kwargs)

        

        


