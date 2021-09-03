from django.urls import path
from . import views

# namespace
app_name = 'mergepdf'

urlpatterns = [
    # Upload pdf, pages need to extract user input, return to the page to be extracted
    path('', views.pdf_extract, name='pdf_extract'),
]