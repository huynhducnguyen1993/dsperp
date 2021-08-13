from django import forms
# from .models import Nhanvien
from django.contrib import admin
from django.forms import widgets
from django.forms.widgets import FileInput
from qlns.models import *
from ckeditor.widgets import CKEditorWidget

class AddnhanvienForm(forms.ModelForm):
    class Meta:
        model = Nhanvien
        fields ='__all__'
        exclue = 'id'
        widgets = {
            'cmnd': forms.TextInput(attrs={'class': 'form-control', 'name': 'cmnd', 'pattern': '[0-9]{1,12}',
                                           'title': 'Cmnd là so có 12 chữ số', 'id': 'cmnd'}),

        }
class AddnhanvienAdmin(admin.ModelAdmin):
    exclude = 'tennv'
    form = AddnhanvienForm

class Changeformnhanvien(forms.ModelForm):
    class Meta:
        model = Nhanvien
        fields ='__all__'
        widgets ={
            'manv':forms.TextInput(attrs={'class':'form-control','name':'manv','id':'manvs'}),
            'tennv': forms.TextInput(attrs={'class': 'form-control', 'name': 'tennv', 'id': 'tennv'}),
            'ngaysinh': forms.DateInput(attrs={'class': 'form-control', 'name': 'ngaysinh', 'id': 'ngaysinh'}),
            'diachi': forms.TextInput(attrs={'class': 'form-control', 'name': 'diachi', 'id': 'diachi'}),
            'quequan': forms.TextInput(attrs={'class': 'form-control', 'name': 'quequan', 'id': 'quequan'}),
            'cmnd': forms.TextInput(attrs={'class': 'form-control', 'name': 'cmnd','pattern':'[0-9]{1,12}' ,'title':'Cmnd là so có 12 chữ số','id': 'cmnd'}),
            'line': forms.TextInput(attrs={'class': 'form-control', 'name': 'line', 'id': 'line'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'name': 'email', 'id': 'email'}),
            'sdt': forms.TextInput(attrs={'class': 'form-control', 'name': 'sdt', 'id': 'sdt'}),



        }
class Deleteformnhanvien(forms.ModelForm):
    class Meta:
        model = Nhanvien
        fields ='__all__'

class Formdexuat(forms.ModelForm):
    class Meta:
        model = Dexuat
        fields =['nhanvien','phongban','hangmuc','noidung','tinhtrangxem','files','guiduyet',]
        widgets ={
            'hangmuc':forms.Select(attrs={'class':'form-control','name':'hangmuc',}),
            'guiduyet':forms.Select(attrs={'class':'form-control','name':'guiduyet'}),
        }
    def __init__(self, *args, **kwargs):
        super(Formdexuat, self).__init__(*args, **kwargs)
class Formdexuat_tp(forms.ModelForm):
    class Meta:
        model = Dexuat
        fields =['trangthaiduyet_tp','tinhtranghuy','tinhtrangxem','ghichu']
    def __init__(self, *args, **kwargs):
        super(Formdexuat_tp, self).__init__(*args, **kwargs)

class Formdexuat_sep(forms.ModelForm):
    class Meta:
        model = Dexuat
        fields =['trangthaiduyet_sep','tinhtranghuy','tinhtrangxem','ghichu']
    
    def __init__(self, *args, **kwargs):
        super(Formdexuat_sep, self).__init__(*args, **kwargs)

class Formedit_dexuat(forms.ModelForm):
    class Meta:
        model = Dexuat
        fields =['hangmuc','tieude','thoigianhoanthanh','files','kinhphi','noidung','ghichu']
        widgets={
            'tieude':forms.TextInput(attrs={'class':'form-control'}),
            'ghichu':forms.TextInput(attrs={'class':'form-control'}),
            'kinhphi':forms.TextInput(attrs={'class':'form-control'}),
            'hangmuc':forms.Select(attrs={'class':'form-control'}),
            'thoigianhoanthanh':forms.DateInput(attrs={'class':'form-control'}),
            'fiels':forms.FileInput(attrs= {'style':'display: none;','class':'form-control', 'required': False,})
        }
    def __init__(self, *args, **kwargs):
        super(Formedit_dexuat, self).__init__(*args, **kwargs)

class Formnhaptamung(forms.ModelForm):
    
    class Meta:
        model = Dexuat
        fields =['tientamung','ghichu','tinhtrangtamung']

    def __init__(self, *args, **kwargs):
        super(Formnhaptamung, self).__init__(*args, **kwargs)


class Formdieuchinhtamung(forms.ModelForm):
    
    class Meta:
        model = Dexuat
        fields =['tientamung','ghichu']

    def __init__(self, *args, **kwargs):
        super(Formdieuchinhtamung, self).__init__(*args, **kwargs)

class Formtaogiaichi_dx(forms.ModelForm):
    
    class Meta:
        model = Giaichi
        fields ='__all__'

    def __init__(self, *args, **kwargs):
        super(Formtaogiaichi_dx, self).__init__(*args, **kwargs)

class Formgiaichi_dexuat(forms.ModelForm):

    class Meta:
        model = Dexuat
        fields = ['tinhtranggiaichi',]
 

class Formxuly_giaichi_tp(forms.ModelForm):
    
    class Meta:
        model = Giaichi 
        fields = ['trangthaiduyet_tp','trangthaihuy','trangthaiduyetgiaichi']

    def __init__(self, *args, **kwargs):
        super(Formxuly_giaichi_tp, self).__init__(*args, **kwargs)

class Formxuly_giaichi_sep(forms.ModelForm):
    
    class Meta:
        model = Giaichi 
        fields = ['trangthaiduyet_sep','trangthaihuy','trangthaiduyetgiaichi']

    def __init__(self, *args, **kwargs):
        super(Formxuly_giaichi_sep, self).__init__(*args, **kwargs)
class Formxuly_giaichi_tckt(forms.ModelForm):
    
    class Meta:
        model = Giaichi 
        fields = ['trangthaiduyet_tckt','trangthaihuy','trangthaiduyetgiaichi']

    def __init__(self, *args, **kwargs):
        super(Formxuly_giaichi_tckt, self).__init__(*args, **kwargs)


class Form_edit_giai_chi(forms.ModelForm):
    
    class Meta:
        model = Giaichi 
        fields = ['guiduyet','ghichu','phongban','tieude','giaichihanghoa','giaichithietbi','giaichikhac','trangthaiduyet_tp','trangthaiduyet_tp','tiengiaichi','filegiaichi']
        
        widgets = {
            'giaichihanghoa':forms.CharField(widget=CKEditorWidget())
            }
    def __init__(self, *args, **kwargs):
        super(Form_edit_giai_chi, self).__init__(*args, **kwargs)

class Form_nhap_giai_chi(forms.ModelForm):
    class Meta:
        model = Giaichi
        fields = ['trangthaihoanthanh','noidungthanhtoan']
    def __init__(self, *args, **kwargs):
        super(Form_nhap_giai_chi, self).__init__(*args, **kwargs)
