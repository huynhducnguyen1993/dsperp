from django import forms
from django.forms import widgets


class PdfUploadForm(forms.Form):
    file = forms.FileField(label="",widget=forms.FileInput(attrs={"class":"form-control"}))
    page = forms.CharField(max_length=20, label="Page Number",widget=forms.TextInput(attrs={"class":"form-control"})) 
class Pdfmerge(forms.Form):
    file = forms.FileField(label=" Chọn File PDF để  Nối ",widget=forms.FileInput(attrs={"class":"form-control","multiple":"multiple"}))
    
