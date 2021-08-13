from django import forms
from django.contrib import admin
from khovan.models import *
from django.forms import ModelForm


class Editnhaphang(ModelForm):
    class Meta:
        model = Phieunhaphang
        fields = "__all__"
        widgets = {
            'thoigiantao':forms.DateInput(attrs={'class':'form-control'}),
            'thoigiannhanhang': forms.DateInput(attrs={'class': 'form-control'}),
            'ghichu':forms.Textarea(attrs={'class':'form-control','rows':'3'})
        }


    def __init__(self, *args, **kwargs):
        super(Editnhaphang, self).__init__(*args, **kwargs)

class Nhapkhoform(ModelForm):
    class Meta:
        model = Nhapkho
        fields ="__all__"
    
    def __init__(self, *args, **kwargs):
        super(Nhapkhoform, self).__init__(*args, **kwargs)
     

class Nhaphangchuaduyetgaps(ModelForm):
    class Meta:
        model = Phieunhaphang
        fields = ['tinhtrang', 'phanhoi', 'tuchoi']
        widgets = {

            'phanhoi': forms.Textarea(attrs={'class': "form-control", 'rows': "3", 'cols': "3"}),

        }

    def __init__(self, *args, **kwargs):
        super(Nhaphangchuaduyetgaps, self).__init__(*args, **kwargs)
class Nhaphangxulykho(ModelForm):
    class Meta:
        model = Phieunhaphang
        fields = ['xulykho']
        widgets = {

            'xulykho': forms.CheckboxInput(attrs={"value":"True","hidden":"True"}),

        }

    def __init__(self, *args, **kwargs):
        super(Nhaphangxulykho, self).__init__(*args, **kwargs)
        self.fields['xulykho'].label =""