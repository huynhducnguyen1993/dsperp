from django.http.response import HttpResponseNotAllowed, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.http.request import QueryDict
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
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
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.core.mail import send_mail
from .forms import *


class Create_khl(LoginRequiredMixin,View):
    login_url="login/"
    def get(self,request):
        usr = request.user
        if usr:
            nhanvien = Nhanvien.objects.get(username =request.user) 
            nvcv  = Chucvu_Congviec.objects.get(nhanvien=nhanvien)
            phongban = Phongban.objects.get(pk = nvcv.phongban.id)
            form = Create_khang_hang_lon(instance = nhanvien)
            context= {
                'nhanvien':nhanvien,
                'phongban':phongban,
                'form':form
            }
            return render(request,"khachhanglon/form_nhap_khach_hang_lon.html",context)
        else:

            return HttpResponse("Bạn Cần Login ")
    def post(self,request):
        usr = request.user
        if request.POST:
            if usr:
                nhanvien = Nhanvien.objects.get(username =request.user) 
                nvcv  = Chucvu_Congviec.objects.get(nhanvien=nhanvien)
                phongban = Phongban.objects.get(pk = nvcv.phongban.id)
                csrf = request.POST.get('csrfmiddlewaretoken')
                
                tinhtrang = request.POST.get('tinhtrang')
                if tinhtrang == "0":
                    bg = True
                    tthd = False
                    khd = False
                if tinhtrang == "1":
                    bg = False
                    tthd = True
                    khd = False
                if tinhtrang == "2":
                    bg = False
                    tthd = False
                    khd = True
                form =  Khachhanglon.objects.create(
                    
                    nhanvien=nhanvien,
                    phongban=phongban,
                    username=usr,
                    hangmuc=request.POST.get('hangmuc'),
                    baogia=bg,
                    thuongthaohopdong=tthd,
                    kyhopdong=khd,
                    huytheo=False,
                    noidung=request.POST.get('noidung'),
                    tenkhachhang=request.POST.get('tenkhachhang'),
                    diachikh=request.POST.get('diachikh'),
                    tencongtrinh=request.POST.get('tencongtrinh'),
                    diachicongtrinh=request.POST.get("diachicongtrinh"),

                )
                
                if form:
                    form.save()
                    
                    messages.success(request,str(request.user.username)+ "-- Đã Cập Nhật khách hàng "+" - -"+request.POST.get('tenkhachhang')+"Thành Công")
                    
                    send_mail(
                        nhanvien.tennv + ' Cập Nhật Khách Hàng Lớn' ,
                        "Dear all \n" + request.POST.get('tencongtrinh')+"\n" + request.POST.get('noidung') +" <a href='#'> Link Xem</a>",
                        '',
                        ['cdldongsapa.@gmail.com'],

                    )
                    return redirect("danh-sach-khach-hang-lon")
                
                else:
                    return HttpResponse("Thêm Khách Hàng Thất Bại")

            else:

                return HttpResponse("Bạn Cần Login ")
        else:
           return HttpResponse("Lỗi Không Mong Muốn") 

class Danhsach_khachhanglon(LoginRequiredMixin,View):
    login_url = "login/"
    def get(self,request):
        usr = request.user 
        if usr:
            khl = Khachhanglon.objects.all().order_by('-id')
            context = {
                'khachhanglon':khl,
            }
            return render(request,"khachhanglon/danh_sach_khach_hang_lon.html",context)
        else:
            return HttpResponse("Lỗi Không Mong Muốn")

class View_khachhanglon(LoginRequiredMixin,View):
    login_url = "login/"
    def get(self,request,khachhang_id):
        usr = request.user 
        if usr:
            khl = Khachhanglon.objects.get(id =khachhang_id)
            context={
                'khachhanglon':khl
            }
            return render(request,"khachhanglon/view_khach_hang_lon.html",context)
        else:
            return HttpResponseNotFound() 


class Edit_khachhanglon(LoginRequiredMixin,View):
    login_url = "login/"
    def get(self,request,khachhang_id):
        usr = request.user 
        if usr:
            khl = Khachhanglon.objects.get(id =khachhang_id)
            if khl and khl.username == usr:
                form = Edit_khang_hang_lon(instance = khl)
                
                context={
                    'khachhanglon':khl,
                    'form':form
                }
                return render(request,"khachhanglon/edit_khach_hang_lon.html",context)
            else:
                return HttpResponseNotAllowed("Không Có quyền")
        else:
            return HttpResponseNotFound("Không có tìm thấy") 

    def post(self,request,khachhang_id):
        usr = request.user

        if usr:
            khl =Khachhanglon.objects.get(pk=khachhang_id)
            if usr == khl.username :
                csrf = request.POST.get('csrfmiddlewaretoken')
                tinhtrang = request.POST.get('tinhtrang')
                nhanvien = Nhanvien.objects.get(username =request.user) 
                nvcv  = Chucvu_Congviec.objects.get(nhanvien=nhanvien)
                phongban = Phongban.objects.get(pk = nvcv.phongban.id)
                if tinhtrang == "0":
                    bg = True
                    tthd = False
                    khd = False
                    tth = False
                if tinhtrang == "1":
                    bg = False
                    tthd = True
                    khd = False
                    tth = False
                if tinhtrang == "2":
                    bg = False
                    tthd = False
                    khd = True
                    tth = False
                if tinhtrang == "3":
                    bg = False
                    tthd = False
                    khd = False
                    tth = True
                querydict = QueryDict("",mutable=True)
                querydict =({
                        'nhanvien':nhanvien,
                        'phongban':phongban,
                        'username':usr,
                        'hangmuc':request.POST.get('hangmuc'),
                        'baogia':bg,
                        'thuongthaohopdong':tthd,
                        'kyhopdong':khd,
                        'huytheo':tth,
                        'noidung':request.POST.get('noidung'),
                        'tenkhachhang':request.POST.get('tenkhachhang'),
                        'diachikh':request.POST.get('diachikh'),
                        'tencongtrinh':request.POST.get('tencongtrinh'),
                        'diachicongtrinh':request.POST.get("diachicongtrinh"),
                })
                form = Edit_khang_hang_lon(querydict,instance = khl)
                if form.is_valid():
                    form.save()
                    messages.success(request,str(request.user.username)+ "-- Đã Cập Nhật Lại khách hàng  "+" - -"+request.POST.get('tenkhachhang')+"Thành Công")
                    
                    return redirect('danh-sach-khach-hang-lon') 
            else:
                return  HttpResponse("Bạn Không Có Quyền")
        else:
            return HttpResponse('Bạn Cần Login')
                
