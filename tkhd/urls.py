from django.urls import path
from . import views
from tkhd.views import *

# namespace
app_name = 'tkhd'

urlpatterns = [
    # Upload pdf, pages need to extract user input, return to the page to be extracted
    path('',Trinhkyhopdong.as_view(), name='trinh-ky-hop-dong'),
]