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


class Loadbangcong(View):
    def get(self,request):
        thang = request.GET.get('thang')
        nam = request.GET.get('nam')
        nhanvien= Nhanvien.objects.get(username =request.user)
        context = {
            'thang':thang,
            'nam':nam,
            'nhanvien':nhanvien

        }
        return render(request,'nhanvien/include/loadbangcong.html',context)

class Loadhoidap(View):
    def get(self,request):
        nvh = Nhanvien.objects.get(username = request.user )
        idpb = request.GET.get('idpb')
        idnv = request.GET.get('nhanvien')
        phongban = Phongban.objects.get(pk=idpb)
        cauhoi = request.GET.get('cauhoi')
        nhanvien=Nhanvien.objects.get(pk=idnv)
        Hoidap.objects.create(idnhanvienhoi = idnv,nhanvienhoi =nhanvien,cauhoi=cauhoi,phongbantraloi = phongban )
        
        hoidap = Hoidap.objects.filter(idnhanvienhoi=nvh.id).order_by('-updated_at')
        context ={
            'hoidap':hoidap,
            'cauhoi':cauhoi,

        }
        return render(request,'nhanvien/include/loadhoidap.html',context)


class Qrcode(View):
    def get(self,request):

        return render(request,'qrcode/index.html')


class loadqrcode(View):
    def get(self,request,*args, **kwargs):
        
        tenwifi = request.GET.get('tenwifi')
        passwifi = request.GET.get('passwifi')
        
        wifi_config = WifiConfig(
                    ssid=tenwifi,
                    authentication=WifiConfig.AUTHENTICATION.WPA,
                    password=passwifi,
                )
        context = dict(
            video_id='J9go2nj6b3M',
            wifi_config=wifi_config,
            options_example=QRCodeOptions(size='t', border=6, error_correction='L'),
        )
        
        


       
        return render(request,'qrcode/loadqrcode.html',context=context )


class Loaddanhba(View):
    def get(self,request):
        phongbans = request.GET.get('phongban')
        keyword = request.GET.get('keyword')
        if keyword =='':
            if phongbans=='0':
                nv = Nhanvien.objects.all().order_by('phongban')
            else:
                pb = Phongban.objects.get(pk=phongbans)
                nv= Nhanvien.objects.filter(phongban=pb)
        
        else:
            nv = Nhanvien.objects.filter(tennv__icontains=keyword)
            print(keyword)
        context = {
            'nv':nv
        }

        return render(request,'nhanvien/danhba/loaddanhba.html',context)