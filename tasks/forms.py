from django import forms
from django.forms import ModelForm, widgets
from django.forms.widgets import NumberInput



from .models import *



class TaskForm(forms.ModelForm):
	CHOICES = (('0', 'Rất Gấp'),('1', 'Gấp'),('2', 'Không Gấp'))
	mucdo = forms.ChoiceField(choices=CHOICES,widget= forms.Select(attrs={'class':'form-control'}))
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Nhập Công việc cần làm..','class':'form-control'}))
	ngayhoanthanh= forms.DateField(widget=NumberInput(attrs={'type':'date','class':'form-control'}))
	
	class Meta:
		model = Task
		fields = '__all__'
		

class TaskForm_complete(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['complete',]


class TaskForm_uncomplete(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['complete',]
