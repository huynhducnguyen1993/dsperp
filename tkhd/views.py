from django.http.request import QueryDict
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.views import View
from django.contrib import messages
from django.http import HttpResponse
import json
from django.shortcuts import get_object_or_404
import datetime
from django.contrib.auth.models import Permission
from django.db.models import Q
from hashlib import sha1

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *

import os
import io
from django.conf import settings


# Create your views here.


class Trinhkyhopdong(View):

    def get(self, request):
        nhanvien =Nhanvien.objects.get(username =request.user) 
        form = Formtrinhky(request)
        dshd =  Tkhd.objects.all()
        
        context= {
            'form':form,
            'nhanvien':nhanvien,
            'phongban':nhanvien.phongban,
            'dshd':dshd,
        }
        return render(request,'tkhd/index.html',context)
    def post(self,request):
        nhanvien =Nhanvien.objects.get(username =request.user) 
        form =Trinhkyhopdong()
        if form:
            post  =  request.POST
            gd = post['guiduyet']
            if gd == '0':
                duyet_at = False
                duyet_tp =False
            if gd == '1':
                duyet_at = True
                duyet_tp = False
            tieude =post['tieude']
            ghichu = post['ghichu']
            khachhang = post['khachhang']
            file = request.FILES['file']
            tk = Tkhd(
                nhanvien=nhanvien,username = request.user,
                khachhang =khachhang,
                phongban=nhanvien.phongban,tieude=tieude,
                guiduyet=gd,trangthaiduyet_tp=duyet_tp,
                trangthaiduyet_at=duyet_at,file=file,ghichu=ghichu
                )
            tk.save()
        return redirect('/trinh-ky-hop-dong/')
