from django.contrib import admin
from django.db import models
from django import forms
from django.forms import widgets
from qlns.models import *
from .forms import *

# Import our custom widget and our model from where they're defined
from .models import *
from qlns.models import *

class CatalogForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = "__all__"




    