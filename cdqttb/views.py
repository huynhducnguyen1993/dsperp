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