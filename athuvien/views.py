from django.http.request import QueryDict
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.views import View
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpResponse
import json
from django.shortcuts import get_object_or_404
import datetime
from django.contrib.auth.models import Permission
from django.db.models import Q
from hashlib import sha1


from rest_framework import status 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from qr_code.qrcode.utils import ContactDetail, WifiConfig, Coordinates, QRCodeOptions
from django.urls import path, include, re_path
from django.conf.urls import url
from django.contrib.postgres.search import SearchVector
import psycopg2
from django.views.generic import ListView
# Create your views here.


class Catolog(View):
    def get(self,request):

        danhmuc = DanhmucCatalog.objects.all()
        hang = HangCatalog.objects.all()
        catalog = Catalog.objects.all()
        context={
            'catalog':catalog,
            'hang':hang,
            'danhmuc':danhmuc,
        }
        return render(request,'thuvien/catolog.html',context)