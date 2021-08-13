from django.http.request import QueryDict
from django.http.response import Http404
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from django.views import View
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NhanvienSerializer
from django.http import HttpResponse
import json
from django.shortcuts import get_object_or_404
import datetime
from django.contrib.auth.models import Permission
from django.db.models import Q


from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
# Create your views here.
class Index(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def get(self,request):
        nv = Nhanvien.objects.all()
        us = User.objects.all()
         

        return render(request,'index.html')

class Login(View):

    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user=user)
            return redirect('index')
        else:
            return render(request,'login.html')

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('login')

class Giaoviec(View):
    def get(self,request):
        return render(request,'kanban.html')


class Report(LoginRequiredMixin,View):

    def get(self,request):

        return render(request,"report.html")

class Nhanvientotal(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def get(self,request):
        nv= Nhanvien.objects.all()

        return render(request, 'nhanvien.html',{'nv':nv})

    def post(self,request):
        if request.method == 'POST':

            manv = request.POST.get('manv')
            tennv= request.POST.get('tennv')
            username = User.objects.get(id=2)
            ngaysinh= request.POST.get('ngaysinh')
            diachi= request.POST.get('diachi')
            quequan= request.POST.get('quequan')
            cmnd = request.POST.get('cmnd')
            cmnd_1 =request.FILES['cmndmt']

            cmnd_2 =request.FILES['cmndms']
            avatar =request.FILES['avatar']
            sdt = request.POST.get('sdt')
            line = request.POST.get('line')
            email = request.POST.get('email')
            
            Nhanvien.objects.create(manv=manv,tennv=tennv,username=username,ngaysinh=ngaysinh,
                                    diachi=diachi, quequan=quequan, cmnd=cmnd,cmnd_1=cmnd_1,
                                    cmnd_2=cmnd_2,avatar=avatar,sdt=sdt,line=line,email=email)
            nv = Nhanvien.objects.all()

            context ={
                'ms':'them thanh cong',
                'nv':nv
            }
            messages.success(request, 'Thêm Thành Cong')
            return redirect('nhanvien')

class Getnhanvien(APIView):

    def get(self,request):
        nv = Nhanvien.objects.all()
        NhanvienSerializer(nv,many=True)
        return Response(nv.data)


class Viewnhanvien(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def get(self,request):
        return redirect('nhanvien')
    def post(self,request):

        nv = Nhanvien.objects.get(id=request.POST.get('idview'))
        context ={
            'nv':nv
        }
        return render(request,'viewnhanvien.html',context)


class Profile(LoginRequiredMixin,View):
    def get(self,request):
        user = request.user
        id = user.id
        nv = Nhanvien.objects.get(username=id)
        idnv = nv.id
        nv =Nhanvien.objects.get(pk=idnv)
        nvcv = Chucvu_Congviec.objects.get(nhanvien= nv)

        try:
            hsld = Hosonhanvien.objects.get(nhanvien=nv.id)
            now_year = datetime.datetime.now().year - hsld.ngaychinhthuc.year

        except Hosonhanvien.DoesNotExist:
            hsld = {'id':'Đang cập nhật','masobh':'Đang cập nhật'}
            now_year="Đang Cập Nhật Số "
        context = {

            'nv': nv,
            'id': id,
            'hsld': hsld,
            'now': now_year,
            'nvcv':nvcv,
        }
        return render(request,'nhanvien/profile.html',context)



class Dsnhanvien(LoginRequiredMixin,View):
    login_url = "login/"
    redirect_field_name = 'redirect_to'
    def get(self,request):
        nv = Nhanvien.objects.all()
        pb = Phongban.objects.get(tenpb = "BÁN SỈ")
        idbs = pb.id

        nvbs = Nhanvien.objects.filter(phongban=idbs)
        nvhcns = Nhanvien.objects.filter(phongban=2)#HCNS
        nvkt = Nhanvien.objects.filter(phongban=1)
        nvit = Nhanvien.objects.filter(phongban=3)
        context={
            'nv':nv,
            'nvhcns':nvhcns,
            'nvkt':nvkt,
            'nvbs':nvbs,
            'nvit':nvit,

        }
        return render(request,'dsnhanvien.html',context)

    def post(self, request):
        tennhanvien = request.POST.get('tennhanvien')
        nvsearch = Nhanvien.objects.filter(tennv__icontains=tennhanvien)
        context = {
            'nvsearch': nvsearch,
        }
        return render(request, 'dsnhanvien.html', context)


class Changenhanvien(LoginRequiredMixin,View):
    login_url = 'login/'
    redirect_field_name = 'redirect_to'
    def get(self,request,nhanvien_id):
        nv = Nhanvien.objects.get(id=nhanvien_id)

        try:
            hsld = Hosonhanvien.objects.get(nhanvien=nv.id)
            now_year = datetime.datetime.now().year - hsld.ngaychinhthuc.year

        except Hosonhanvien.DoesNotExist:
            hsld = {'id':'Đang cập nhật','masobh':'Đang cập nhật'}
            now_year="Đang Cập Nhật Số "
        context={
                'nv': nv,
                'id': nhanvien_id,
                'hsld': hsld,
                'now': now_year
            }

        return render(request, 'xemnhanvien.html', context)

    def post(self,request,nhanvien_id):
        if request.method == 'POST':
            form = Nhanvien.objects.get(id=nhanvien_id)

            form = Changeformnhanvien(request.POST, request.FILES , instance=form)


            if request.POST['change']:
                if form.is_valid():
                    form.save()

        return redirect('nhanvien')


class Deletenhanvien(View):
    def get(self,request,nhanvien_id):
        form = Nhanvien.objects.get(id=nhanvien_id)
        form.delete()
        return redirect('nhanvien')


class Phieuluongupload(LoginRequiredMixin,View):
    login_url = 'login/'
    redirect_field_name = 'redirect_to'
    def get(self,request):
        pl = Phieuluong_upload.objects.all()
        context ={
            'pl':pl,
            'thang':[1,2,3,4,5,6,7,8,9,10,11,12],
            'nam':[2021,2022,2023],
        }
        return render(request,'phieuluongupload.html',context)

    def post(self,request):
        thang = request.POST.get('thang')
        nam = request.POST.get('nam')
        try:

            pl = Phieuluong_upload.objects.filter(thang=thang,nam=nam)

        except Phieuluong_upload.DoesNotExist:
            pl = Phieuluong_upload.objects.all()


        context = {
            'pl': pl,
            'thang': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            'nam': [2020,2021, 2022, 2023],
        }
        return render(request,'phieuluongupload.html',context)

class Phieuluongcanhan(LoginRequiredMixin,View):
    login_url = 'login/'
    redirect_field_name = 'redirect_to'
    def get(self,request,nhanvien_id):
        pl = Phieuluong_upload.objects.filter(pk=nhanvien_id)

        context = {
            'pl': pl,
            'thang': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            'nam': [2020, 2021, 2022, 2023],

        }
        return render(request, 'phieuluongcanhan.html', context)


class Phieuluonguser(LoginRequiredMixin,View):
    login_url = 'login/'
    redirect_field_name = 'redirect_to'
    def get(self,request):
        user = request.user
        id = user.id
        nv = Nhanvien.objects.get(username=id)
        idnv =nv.id

        pl = Phieuluong_upload.objects.filter(nhanvien=idnv).order_by('-nam','-thang')
        context={
            'user':user,
             'pl':pl,
            'thang': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            'nam': [2020, 2021, 2022, 2023],
        }


        return render(request,'phieuluonguser.html',context)

    def post(self,request):
        nam = request.POST.get('nam')
        thang = request.POST.get('thang')
        if nam == 100 and thang == 100:
            messages.error(request,"Chọn Tháng Năm Để Loc")
        else:
            user = request.user
            id = user.id
            nv = Nhanvien.objects.get(username=id)
            idnv = nv.id

        pl = Phieuluong_upload.objects.filter(nhanvien=idnv, nam=nam, thang=thang)
        context = {

            'pl': pl,
            'thang': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            'nam': [2020, 2021, 2022, 2023],
        }

        return render(request, 'phieuluonguser.html', context)

class Thoiviecnhanvien(View):
    pass


class Delete_checkbox(View):
    def get(self,request):
        all = Nhanvien.objects.all()
        context={
            'nv':all
        }
        return render(request, 'deletenhanvien.html',context)
    def post(self,request):
        if request.method == "POST":
            print("Hello")



        return redirect('nhanvien')


class Dexuats(LoginRequiredMixin,View):
    login_url='login/'
    redirect_field_name = 'redirect_to'
    def get(self,request):
        user = request.user
        nhanvien = Nhanvien.objects.get(username=user)
        phongban = Phongban.objects.get(tenpb=nhanvien.phongban)
        form = Formdexuat(request.POST)
        
        context={

            'nhanvien':nhanvien,
            'phongban':phongban,
            'form':form,

        }
        return render(request,'dexuat/form_de_xuat.html',context)

    def post(self,request):
        print( request.FILES['files'])
        if request.POST:
            if request.FILES['files']:
                user = request.user
                us = User.objects.filter(username = user).first
                nv = Nhanvien.objects.get(username=user)
                pb = Phongban.objects.get(tenpb=nv.phongban)
                files = request.FILES['files']
                tg = request.POST.get('thoigiandukien')
                
                noidung = request.POST.get('noidung')  
                kp = request.POST.get('kinhphi')
                gc = request.POST.get('ghichu')
                hmdx = request.POST.get('hangmuc')
                guiduyet = request.POST.get('guiduyet')
                tieude = request.POST.get('tieude')
                if int(guiduyet) == 0:
                    ttp = False
                    tts = False
                if int(guiduyet) == 1:
                    ttp = False
                    tts = True    
                
                Dexuat.objects.create(nhanvien=nv,
                                    phongban=pb,
                                    tieude=tieude,
                                    noidung=noidung,
                                    username =request.user,
                                    files=files,
                                    guiduyet=guiduyet,
                                    hangmuc=hmdx,
                                    trangthaiduyet_tp=ttp,
                                    trangthaiduyet_sep=tts,
                                    tinhtrangxem=False,
                                    tinhtranghuy=False,
                                    tinhtrangtamung=False,
                                    kinhphi=kp,
                                    ghichu=gc,
                                    thoigianhoanthanh=tg,
                                    tientamung=0,
                                    )
                
                return redirect("dexuat-chua-duyet")
            if  request.FILES['files']=="":
                user = request.user
                us = User.objects.filter(username = user).first
                nv = Nhanvien.objects.get(username=user)
                pb = Phongban.objects.get(tenpb=nv.phongban)
                
                tg = request.POST.get('thoigiandukien')
                
                files =''

                noidung = request.POST.get('noidung')  
                kp = request.POST.get('kinhphi')
                gc = request.POST.get('ghichu')
                hmdx = request.POST.get('hangmuc')
                guiduyet = request.POST.get('guiduyet')
                tieude = request.POST.get('tieude')
                if int(guiduyet) == 0:
                    ttp = False
                    tts = False
                if int(guiduyet) == 1:
                    ttp = False
                    tts = True    
                
                Dexuat.objects.create(nhanvien=nv,
                                    phongban=pb,
                                    tieude=tieude,
                                    noidung=noidung,
                                    username =request.user,
                                    files=files,
                                    guiduyet=guiduyet,
                                    hangmuc=hmdx,
                                    trangthaiduyet_tp=ttp,
                                    trangthaiduyet_sep=tts,
                                    tinhtrangxem=True,
                                    tinhtranghuy=False,
                                    tinhtrangtamung=False,
                                    kinhphi=kp,
                                    ghichu=gc,
                                    thoigianhoanthanh=tg,
                                    tientamung=0,
                                    )
                
                return redirect("dexuat-chua-duyet")


class Dexuatchuaduyet(LoginRequiredMixin,View):
    login_url ="login/"
    redirect_field_name = 'redirect_to'
    def get(self,request):
        
        dexuat = Dexuat.objects.filter(Q(trangthaiduyet_tp = False)| Q(trangthaiduyet_sep=False),
                                        tinhtranghuy = False,username =request.user
                                        
                                        
                                        ).order_by('created_at','id')
        context ={
            'dexuat':dexuat,
        }                                
        return render(request,'dexuat/dexuat_chua_duyet.html',context)

class Dexuatdaduyet(LoginRequiredMixin,View):
    login_url ="login/"
    redirect_field_name = 'redirect_to'
    def get(self,request):
        
        dexuat = Dexuat.objects.filter( 
                                        username = request.user,
                                        trangthaiduyet_tp = True,
                                        trangthaiduyet_sep = True,
                                        tinhtrangxem = True,
                                        tinhtranghuy = False,
                                        )
        context ={
            'dexuat':dexuat,
        }                                
        return render(request,'dexuat/dexuat_da_duyet.html',context)

class Dexuathuy(LoginRequiredMixin,View):
    login_url ="/login/"
    redirect_field_name = 'redirect_to'
    def get(self,request):
        
        dexuat = Dexuat.objects.filter( username = request.user,tinhtranghuy = True,
                                        )
        context ={
            'dexuat':dexuat,
        }                                
        return render(request,'dexuat/dexuat_huy.html',context)

class Quanlydexuat(LoginRequiredMixin,View):
    login_url ="login/"
    def get(self,request):
        user = request.user 
        pb = Phongban.objects.all()
        nv = Nhanvien.objects.get(username = user)
        cv = Chucvu_Congviec.objects.filter(phongban=nv.phongban)
        for item in cv:
            if str(item.tencongviec) == "TP":
                dx =Dexuat.objects.filter(
                                  phongban = item.phongban,
                                  trangthaiduyet_tp = False,
                                  
                                  
                                  tinhtranghuy = False,
                                  )

                context ={
                    
                    'dexuat':dx,
                      }
                return render(request,'dexuat/ql_dexuat_cho_xu_ly.html',context)
            else:
                return HttpResponse("Bạn Không Có Thẩm Quyền : <a href='javascript:history.back()")
class Quanlydexuat_sepduyet(LoginRequiredMixin,View):
    login_url ="login/"
    def get(self,request):
        user = request.user
        if str(user)  == "phuhuu":
            pb = Phongban.objects.all()
            dx = Dexuat.objects.filter(
                                    trangthaiduyet_tp = True,
                                    trangthaiduyet_sep = False,
                                    
                                    tinhtranghuy = False,
                                    )

            context ={
                'phongban':pb,
                'dexuat':dx,
            }
            return render(request,'dexuat/ql_dexuat_cho_sep_xu_ly.html',context)
        else:
            return HttpResponse("<strong>Bạn Không có Quyền :</strong> <a href='javascript:history.back()'> Quay lại</a> ")

class Quanlydexuat_daduyet(LoginRequiredMixin,View):
    login_url ="login/"
    def get(self,request):
        user =request.user 
        if str(user) == "phuhuu":
            pb = Phongban.objects.all()
            dx = Dexuat.objects.filter(
                                  trangthaiduyet_tp = True,
                                  trangthaiduyet_sep = True,
                                  
                                  tinhtranghuy = False,
                                  )
            context ={
                'phongban':pb,
                'dexuat':dx,
                }
            return render(request,'dexuat/ql_dexuat_da_xu_ly.html',context)
        else:
            nv = Nhanvien.objects.get(username = user)
            cv = Chucvu_Congviec.objects.filter(phongban=nv.phongban)
            for item in cv:
                if str(item.tencongviec) == "TP":
                
                    dx = Dexuat.objects.filter(
                                  phongban = item.phongban,
                                  trangthaiduyet_tp = True,
                                  trangthaiduyet_sep = True,
                            
                                  tinhtranghuy = False,
                                  )
                    context ={
                
                        'dexuat':dx,
                        }
                    return render(request,'dexuat/ql_dexuat_da_xu_ly.html',context) 
class Quanlydexuat_datamung(LoginRequiredMixin,View):
    login_url ="login/"
    def get(self,request):
        user = request.user 
        if str(user) == "phuhuu": 
            
            pb = Phongban.objects.all()
            dx = Dexuat.objects.filter( trangthaiduyet_tp = True,
                                  trangthaiduyet_sep = True,
                                  tinhtrangtamung=True,
                                  tinhtranghuy = False,
                                  ).exclude(tientamung=0)
        
            context ={
                'phongban':pb,
                'dexuat':dx
            }
            return render(request,'dexuat/ql_dexuat_da_tam_ung.html',context)
        
        if str(user) != "phuhuu": 
            nv = Nhanvien.objects.get(username = user)
            cv = Chucvu_Congviec.objects.filter(phongban=nv.phongban)
            for item in cv:
                if str(item.tencongviec) == "TP":
                    dx = Dexuat.objects.filter(
                                  phongban = item.phongban,
                                  trangthaiduyet_tp = True,
                                  trangthaiduyet_sep = True,
                                  
                                  tinhtranghuy = False,
                                  ).exclude(tientamung=0)
        
                    context ={
                
                            'dexuat':dx
                        }
                    return render(request,'dexuat/ql_dexuat_da_tam_ung.html',context)

class Quanlydexuat_dagiaichi(LoginRequiredMixin,View):
    login_url ="login/"
    def get(self,request):
        user = request.user 
        if str(user) == "phuhuu": 
            
            pb = Phongban.objects.all()
            dx = Giaichi.objects.filter( trangthaiduyet_tp = True,
                                  trangthaiduyet_sep = True,
                                  trangthaiduyetgiaichi=True,
                                  trangthaihuy = False,
                                  )
        
            context ={
                'phongban':pb,
                'dexuat':dx
            }
            return render(request,'dexuat/ql_dexuat_da_tam_ung.html',context)
        
        if str(user) != "phuhuu": 
            nv = Nhanvien.objects.get(username = user)
            cv = Chucvu_Congviec.objects.filter(phongban=nv.phongban)
            for item in cv:
                if str(item.tencongviec) == "TP":
                    dx = Giaichi.objects.filter(
                                  phongban = item.phongban,
                                  trangthaiduyet_tp = True,
                                  trangthaiduyet_sep = True,
                                  trangthaiduyetgiaichi=True,
                                  trangthaihuy = False,
                                  )
        
                    context ={
                
                            'dexuat':dx
                        }
                    return render(request,'dexuat/ql_dexuat_da_giai_chi.html',context)
    

class Quanlydexuat_dahuy(LoginRequiredMixin,View):
    login_url ="login/"
    def get(self,request):
        pb = Phongban.objects.all()
        dx = Dexuat.objects.filter(
                                  
                                  tinhtranghuy = True,
                                  )
        context ={
            'phongban':pb,
            'dexuat':dx,
        }
        return render(request,'dexuat/ql_dexuat_da_huy.html',context)
 
class View_dexuat(LoginRequiredMixin,View):
    login='login/'
    def get(self,request,dexuat_id):
        dx = Dexuat.objects.get(pk=dexuat_id)
        user =str(request.user)
        us = User.objects.get(username = user)
        nv = Nhanvien.objects.get(username=us)
        cv = Chucvu_Congviec.objects.filter(phongban=nv.phongban)
       
        for item in cv:
            if str(item.tencongviec)  == "TP" :
                gc = Giaichi.objects.all()
                if nv.phongban == dx.phongban :
                    form = Formdexuat_sep(request.POST)
                    dexuat = Dexuat.objects.filter(id=dexuat_id,phongban = nv.phongban ).first
                    context = { 
                        "form":form,
                        "nhanvien":nv,
                        'dexuat':dexuat,
                         }
                    return render(request,'dexuat/view_dexuat.html',context)
                else:
                    return HttpResponse("<strong>Bạn Không có Quyền</strong> <a href='javascript:history.back()'> Quay lại</a> ")

            if str(item.tencongviec)  == "SEP" :
                form = Formdexuat_sep(request.POST)
                dexuat = Dexuat.objects.get(pk=dexuat_id)
                context = { 
                    "form":form,
                    "nhanvien":nv,
                    'dexuat':dexuat,
                }
                return render(request,'dexuat/view_dexuat.html',context)
        
        if user == dx.username.username:
            form = Formdexuat_sep(request.POST)
            dexuat = Dexuat.objects.get(pk=dexuat_id)
            context = { 
                    "form":form,
                    "nhanvien":nv,
                    'dexuat':dexuat,
                }
            return render(request,'dexuat/view_dexuat.html',context)
        else:
            return HttpResponse("<strong>Bạn Không có Quyền</strong> <a href='javascript:history.back()'> Quay lại</a> ")

class Xulyduyet_tp(LoginRequiredMixin,View):
    def get(self,request,dexuat_id):
        form = Formdexuat_tp(request.POST)
        dexuat = Dexuat.objects.get(pk=dexuat_id)
        us = User.objects.get(username = request.user)
        nhanvien = Nhanvien.objects.get(username=us)
        context ={
            "form":form,
            'dexuat':dexuat,
            'nhanvien':nhanvien,
        }
        return render(request,'dexuat/form_duyet_tp.html',context)
    def post(self,request,dexuat_id):

        if request.POST:
            csrf = request.POST.get('csrfmiddlewaretoken')
            value_ttp =int(request.POST.get('tinhtrangduyet_tp'))
            
            if value_ttp == 1:
                ttp = True
                tth = False
            if value_ttp == 0:
                ttp = False
                tth = True
            ghichu = request.POST.get('ghichu')   
            dx= Dexuat.objects.get(pk=dexuat_id)
            querydict = QueryDict("",mutable=True)
            querydict.update(
                {
                    'csrfmiddlewaretoken':csrf,
                    'trangthaiduyet_tp':ttp,
                    'tinhtranghuy':tth,
                    'tinhtrangxem':True,
                    'ghichu':ghichu,
                }
            )
            form =Formdexuat_tp(querydict,instance=dx)
            if form.is_valid():
                form.save()
                messages.success(request,"Đã Hoàn Thành")
            return redirect('quan-ly-de-xuat')

class Xulyduyet_sep(LoginRequiredMixin,View):
    login='login/'
    def get(self,request,dexuat_id):
        user =str(request.user)
        if user  =="phuhuu":
            form = Formdexuat_sep(request.POST)
            dexuat = Dexuat.objects.get(pk=dexuat_id)
            us = User.objects.get(username = request.user)
            nhanvien = Nhanvien.objects.get(username=us)
            context = { 
                "form":form,
                'dexuat':dexuat,
                'nhanvien':nhanvien,
            }
            return render(request,'dexuat/form_duyet_sep.html',context)
        else:
            return HttpResponse("<strong>Bạn Không có Quyền</strong> <a href='javascript:history.back()'> Quay lại</a> ")

    def post(self,request,dexuat_id):

        if request.POST:
            csrf = request.POST.get('csrfmiddlewaretoken')
            value_tts =int(request.POST.get('tinhtrangduyet_sep'))
            
            if value_tts == 1:
                tts = True
                tth =False
            if value_tts == 0:
                tts = False
                tth = True
            ghichu = request.POST.get('ghichu')   
            dx= Dexuat.objects.get(pk=dexuat_id)
            querydict = QueryDict("",mutable=True)
            querydict.update(
                {
                    'csrfmiddlewaretoken':csrf,
                    'trangthaiduyet_sep':tts,
                    'tinhtranghuy':tth,
                    'tinhtrangxem':True,
                    'ghichu':ghichu,
                }
            )
            form = Formdexuat_sep(querydict,instance=dx)
            if form.is_valid():
                form.save()
                messages.success(request,"Đã Hoàn Thành")
            return redirect('quan-ly-de-xuat-sep')

class Editdexuat(LoginRequiredMixin,View):
    login_url="login/"

    def get(self,request,dexuat_id):
        try:
            dx = Dexuat.objects.filter(id=dexuat_id,trangthaiduyet_tp=False,trangthaiduyet_sep=False,username=request.user).first
            dexuat = Dexuat.objects.get(pk=dexuat_id)
            form = Formedit_dexuat(instance=dexuat)
            nhanvien = Nhanvien.objects.filter(username =request.user).first
            if request.user == dexuat.username :
                if dx:
                    context ={
                        'dexuat':dexuat,
                        'form':form,
                        'nhanvien':nhanvien
                    }
                    return render(request,"dexuat/edit_dexuat.html",context)
            else:
                return HttpResponse("Bạn Không Có Quyền Sửa  : <a href='javascript:history.back()'> Quay Lại</a>")

        except Dexuat.DoesNotExist:
            return HttpResponse("Bạn Không Có Quyền Sửa : <a href='javascript:history.back()'>Quay Lại</a>")

    def post(self,request,dexuat_id):
        try:
            dx = Dexuat.objects.filter(id=dexuat_id,trangthaiduyet_tp=False,trangthaiduyet_sep=False,username=request.user).first
            dexuat = Dexuat.objects.get(pk=dexuat_id)
            
            nhanvien = Nhanvien.objects.filter(username =request.user).first
            
            if request.user == dexuat.username :
                if request.POST:
                    form = Formedit_dexuat(request.POST,request.FILES,instance=dexuat)
                    if form.is_valid():
                        form.save()

                return redirect('dexuat-chua-duyet')

            else:
                return HttpResponse("Bạn Không Có Quyền Sửa  : <a href='javascript:history.back()'> Quay Lại</a>")

        except Dexuat.DoesNotExist:
            return HttpResponse("Bạn Không Có Quyền Sửa : <a href='javascript:history.back()'>Quay Lại</a>")
    

class Nhaptamung(LoginRequiredMixin,View):
    login_url="login/"

    def get(self,request):
        pb = Phongban.objects.all()
        dx = Dexuat.objects.filter(
                                  trangthaiduyet_tp = True,
                                  trangthaiduyet_sep = True,
                                  tinhtranggiaichi = False,
                                  tientamung =0,
                                  tinhtranghuy = False,
                                  ).order_by("created_at")
        context ={
            'phongban':pb,
            'dexuat':dx,
        }
        return render(request,"thuquy/nhap-tam-ung.html",context)
    
    
class Datamung(LoginRequiredMixin,View):
    login_url="login/"

    def get(self,request):
        pb = Phongban.objects.all()
        
        dx = Dexuat.objects.filter(
                                  trangthaiduyet_tp = True,
                                  trangthaiduyet_sep = True,
                                  tinhtranggiaichi = False,
                                  tinhtrangtamung=True,
                                  tinhtranghuy = False,
                                  ).exclude(tientamung=0)
        context ={
            'phongban':pb,
            'dexuat':dx,
        }
        return render(request,"thuquy/da-tam-ung.html",context)

class Formnhap_tamung(LoginRequiredMixin,View):
    login_url ="login/"
    def get(self,request,dexuat_id):
        user = request.user.is_authenticated
        dx = Dexuat.objects.get(pk=dexuat_id)
        if dx.tinhtranggiaichi == False:
            nv = Nhanvien.objects.get(username = user) 
            context = {
                'dexuat':dx,
                'nhanvien':nv,
            }
            return render(request,'thuquy/form_nhap_tam_ung.html',context)

        if dx.tinhtranggiaichi == True:
            return HttpResponse("Đề Xuất Đã Giải Chi <a href='javascript:history.back()'>Quay Lại</a>")


    def post(self,request,dexuat_id):
        
        csrf = request.POST.get('csrfmiddlewaretoken')
        dx = Dexuat.objects.get(pk=dexuat_id)
        querydict = QueryDict("",mutable=True)
        ghichu = request.POST.get('ghichu') 
        tientamung = int(request.POST.get('tientamung'))
        if tientamung > 0:
            ttu =True
        else:
            ttu =False
        querydict.update(
                {
                    'csrfmiddlewaretoken':csrf,
                    'tientamung':tientamung,
                    'ghichu':ghichu,
                    'tinhtrangtamung':ttu,
                }
            )
        form = Formnhaptamung(querydict,instance=dx)
        if form.is_valid():
            form.save()
        return redirect('nhap-tam-ung')

class Formdieuchinh_tamung(LoginRequiredMixin,View):
    login_url ="login/"
    def get(self,request,dexuat_id):
        user = request.user.is_authenticated
        dx = Dexuat.objects.get(pk=dexuat_id)
        nv = Nhanvien.objects.get(username = user) 
        context = {
            'dexuat':dx,
            'nhanvien':nv,
        }
        return render(request,'thuquy/form_dieu_chinh_tam_ung.html',context)
    
    def post(self,request,dexuat_id):
        
        csrf = request.POST.get('csrfmiddlewaretoken')
        dx = Dexuat.objects.get(pk=dexuat_id)
        querydict = QueryDict("",mutable=True)
        ghichu = request.POST.get('ghichu') 
        tientamung = int(request.POST.get('tientamung'))
        if tientamung > 0:
            ttu =True
        else:
            ttu =False
        querydict.update(
                {
                    'csrfmiddlewaretoken':csrf,
                    'tientamung':tientamung,
                    'ghichu':ghichu,
                    'tinhtrangtamung':ttu,
                }
            )
        form = Formdieuchinhtamung(querydict,instance=dx)
        if form.is_valid():
            form.save()
        return redirect('da-tam-ung')


class Taogiaichi(LoginRequiredMixin,View):
    login_url="login/"
    def get(self,request):
        user = request.user
        dx = Dexuat.objects.filter(
                                  username = user,
                                  trangthaiduyet_tp = True,
                                  trangthaiduyet_sep = True,
                                  tinhtranggiaichi = False,
                                  tinhtranghuy = False,
                                  )
        context ={
            
            'dexuat':dx,
        }
        

        return render(request,"giaichi/tao_giai_chi.html",context)

class Giaichi_dx(LoginRequiredMixin,View):

    login_url="login/"

    def get(self,request,dexuat_id):

        user = request.user
        #form = Formtaogiaichi_dx({"noidunggiaichi":"<table align='center' border='1' cellpadding='1' cellspacing='1' class='table_giai_chi' id='table_giai_chi'  style='height:288px; width:786px'><caption>Nội Dung Giải Chi</caption><tbody><tr style='background-color: rgb(57, 201, 245);'><td style='background-color:#3399ff'><h2>STT</h2></td><td style='background-color:#3399ff'><h2>SBN</h2></td><td style='background-color:#3399ff'><h2>Nội Dung H&agrave;ng H&oacute;a</h2></td><td style='background-color:#3399ff'><h2>Số lượng</h2></td><td style='background-color:#3399ff'><h2>Đơn Gi&aacute;</h2></td><td style='background-color:#3399ff'><h2>Th&agrave;nh Tiền</h2></td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td colspan='5' rowspan='1'><span style='color:#3498db'><strong>Tổng</strong></span></td><td>&nbsp;</td></tr></tbody></table><p>&nbsp;</p><p>&nbsp;</p><style>#table_giai_chi{color:red; foat:left;} </style> "})
        form = Formtaogiaichi_dx()       
        gc = Dexuat.objects.get(pk=dexuat_id)
        if gc.username == user:
            if gc.tinhtranggiaichi ==False:
                nv = Nhanvien.objects.filter(username =gc.username).first
                phongban = Phongban.objects.all()
                context ={
                    'nhanvien':nv,
                    'giaichi':gc,
                    'phongban':phongban,
                    'form':form,
                }
                return render(request,"giaichi/form_giai_chi_dx.html",context)
            else:
                return HttpResponse("Đã Giải Chi : <a href='javascript:history.back()'>Quay Lại</a>")
        else:
            return HttpResponse("Bạn Không Có Quyền : <a href='javascript:history.back()'>Quay Lại</a>")
    def post(self,request,dexuat_id):
        form = Formtaogiaichi_dx(request.POST)
        user = request.user 
        gc = Dexuat.objects.get(pk=dexuat_id)
        if gc.username == user :
            file = request.FILES['filegiaichi']
            id_pb =request.POST.get('phongbanguiduyet')
            p = Phongban.objects.get(pk=id_pb)
            ghichu =request.POST.get('ghichu')
            tiengiaichi = request.POST.get('tiengiaichi')
            gd = request.POST.get('guiduyet')
            
            if gd == '0':
                tpd = False
                sd = False
                tckt = False
            if gd == '2':
                tpd = False
                tckt = False
                sd= True  

            if gc.hangmuc == "0":
                Giaichi.objects.create(
                                        dexuat=gc,
                                        trangthaiduyet_tp=tpd,
                                        trangthaiduyet_sep=sd,
                                        trangthaiduyet_tckt=tckt,
                                        trangthaiduyetgiaichi=False,
                                        trangthaihuy = False,
                                        guiduyet=request.POST.get('guiduyet'),
                                        trangthaihoanthanh =False,
                                        nhanvien=gc.nhanvien,
                                        phongban = p,
                                        username = gc.username,
                                        noidungdexuat = gc.noidung,
                                        tieude=gc.tieude,
                                        hangmuc=0,
                                        ghichu = ghichu,
                                        filegiaichi =file,
                                        tientamung = gc.tientamung,
                                        tiengiaichi = tiengiaichi,
                                        giaichithietbi = None,
                                        giaichihanghoa = request.POST.get('giaichihanghoa'),
                                        giaichikhac=None,
                                    )
            if gc.hangmuc == "1":
                if request.method == "POST":
                    gc = Dexuat.objects.get(pk=dexuat_id)
                    sl1 =  int(request.POST.get('soluong_1'))
                    sl2 =  int(request.POST.get('soluong_2'))
                    sl3 =  int(request.POST.get('soluong_3'))
                    sl4 =  int(request.POST.get('soluong_4'))
                    sl5 =  int(request.POST.get('soluong_5'))
                    dg1 =  int(request.POST.get('dongia_1'))
                    dg2 =  int(request.POST.get('dongia_2'))
                    dg3 =  int(request.POST.get('dongia_3'))
                    dg4 =  int(request.POST.get('dongia_4'))
                    dg5 =  int(request.POST.get('dongia_5'))
                    tt1 =  sl1*dg1
                    tt2 =  sl2*dg2
                    tt3 =  sl3*dg3
                    tt4 =  sl4*dg4
                    tt5 =  sl5*dg5
                    tiengiaichi = tt1+tt2+tt3+tt4+tt5
                    
                    file = request.FILES['filegiaichi']
                    u = User.objects.get(username=request.user)
                    id_pb =request.POST.get('phongbanguiduyet')
                    p = Phongban.objects.get(pk=id_pb)
                    nv = Nhanvien.objects.get(username = u)
                    tgc = request.POST.get('tgc')
                    ghichu =request.POST.get('ghichu')
                    noidung = {
                                'hanghoa_1':request.POST.get('hanghoa_1'),
                                'soluong_1':request.POST.get('soluong_1'),
                                'dongia_1':request.POST.get('dongia_1'),
                                'thanhtien_1':tt1,
                                'hanghoa_2':request.POST.get('hanghoa_2'),
                                'soluong_2':request.POST.get('soluong_2'),
                                'dongia_2':request.POST.get('dongia_2'),
                                'thanhtien_2':tt2,
                                'hanghoa_3':request.POST.get('hanghoa_3'),
                                'soluong_3':request.POST.get('soluong_3'),
                                'dongia_3':request.POST.get('dongia_3'),
                                'thanhtien_3':tt3,
                                'hanghoa_4':request.POST.get('hanghoa_4'),
                                'soluong_4':request.POST.get('soluong_4'),
                                'dongia_4':request.POST.get('dongia_4'),
                                'thanhtien_4':tt4,
                                'hanghoa_5':request.POST.get('hanghoa_5'),
                                'soluong_5':request.POST.get('soluong_5'),
                                'dongia_5':request.POST.get('dongia_5'),
                                'thanhtien_5':tt5,
                            }
                    gd = request.POST.get('guiduyet')
                    if gd:
                        if int(gd) == 0:
                            tpd = False
                            sd = False
                        if int(gd) == 1:
                            tpd = False
                            sd= True  
                    id_pb =request.POST.get('phongbanguiduyet')
                    p = Phongban.objects.get(pk=id_pb)
                    Giaichi.objects.create(
                        dexuat=gc,
                        trangthaiduyet_tp=tpd,
                        trangthaiduyet_tckt=True,
                        trangthaiduyet_sep=sd,
                        trangthaiduyetgiaichi=False,
                        trangthaihuy = False,
                        trangthaihoanthanh =False,
                        nhanvien=nv,
                        hangmuc = 1,
                        guiduyet = request.POST.get('guiduyet'),
                        phongban = p,
                        username = request.user,
                        noidungdexuat=gc.noidung,
                        tieude=gc.tieude,
                        ghichu =ghichu,
                        filegiaichi =file,
                        tientamung = gc.tientamung,
                        tiengiaichi = tiengiaichi,
                        giaichihanghoa=None,
                        giaichithietbi = noidung,
                        giaichikhac=None,
                    )

            if gc.hangmuc == "2":
                Giaichi.objects.create(
                                        dexuat=gc,
                                        trangthaiduyet_tp=tpd,
                                        trangthaiduyet_tckt=True,
                                        trangthaiduyet_sep=sd,
                                        trangthaiduyetgiaichi=False,
                                        trangthaihuy = False,
                                        trangthaihoanthanh =False,
                                        guiduyet=request.POST.get('guiduyet'),
                                        nhanvien=gc.nhanvien,
                                        hangmuc = 2,
                                        phongban = p,
                                        username = gc.username,
                                        noidungdexuat=gc.noidung,
                                        tieude=gc.tieude,
                                        ghichu = ghichu,
                                        filegiaichi =file,
                                        tientamung = gc.tientamung,
                                        tiengiaichi = tiengiaichi,
                                        giaichithietbi = None,
                                        giaichikhac = request.POST.get('giaichihanghoa'),
                                        giaichihanghoa = None
                                    )
            csrf = request.POST.get('csrfmiddlewaretoken')
            querydict = QueryDict("",mutable=True)

            querydict.update(
                    {
                        'csrfmiddlewaretoken':csrf,
                        'tinhtranggiaichi':True,  
                    }
                )
            formdx  = Formgiaichi_dexuat(querydict,instance=gc)
            
            if formdx.is_valid():
                formdx.save()
            
            return redirect("tao-giai-chi")
        
        else:
            return HttpResponse("Bạn Không Có Quyền  : <a href='javascript:history.back()' >Quay Lại</a>")

class Giaichihanghoa_moi(LoginRequiredMixin,View):
    login_url="login/"
    def get(self,request):
        user = request.user
        form = Formtaogiaichi_dx()
        nv = Nhanvien.objects.filter(username =user).first
        phongban = Phongban.objects.all()
        
        context ={
            'nhanvien':nv,
            'form':form,
            'phongban':phongban,
        }
        return render(request,"giaichi/form_giai_chi_hang_hoa_moi.html",context)
    
    def post(self,request):
        
        gc = None
        file = request.FILES['filegiaichi']
        u = User.objects.get(username=request.user)
        id_pb =request.POST.get('phongbanguiduyet')
        p = Phongban.objects.get(pk=id_pb)
        nv = Nhanvien.objects.get(username = u)

       
        ghichu =request.POST.get('ghichu')
        gd = request.POST.get('guiduyet')
        if gd:
            if int(gd) == 0:
                tpd = False
                tckt = False
                sd = False
            if int(gd) == 2:
                tpd = False
                tckt=False
                sd= True  
        Giaichi.objects.create(
            dexuat=gc,
            hangmuc=request.POST.get('hangmuc'),
            trangthaiduyet_tp=tpd,
            trangthaiduyet_tckt=tckt,
            trangthaiduyet_sep=sd,
            trangthaiduyetgiaichi=False,
            trangthaihuy = False,
            trangthaihoanthanh =False,
            guiduyet=request.POST.get('guiduyet'),
            nhanvien=nv,
            phongban = p,
            username = request.user,
            giaichihanghoa=request.POST.get('giaichihanghoa'),
            giaichithietbi = None,
            giaichikhac=None,
            noidungdexuat=None,
            tieude=request.POST.get('tieude'),
            ghichu =ghichu,
            filegiaichi = file,
            tientamung = 0,
            tiengiaichi = request.POST.get('tiengiaichi'),
           
        )

        return render(request,"giaichi/tao_giai_chi.html")

class Giaichikhac_moi(LoginRequiredMixin,View):
    login_url="login/"
    redirect_field_name = 'redirect_to'
    def get(self,request):
        user = request.user
        form = Formtaogiaichi_dx()
        nv = Nhanvien.objects.filter(username =user).first
        phongban = Phongban.objects.all()
        
        context ={
            'nhanvien':nv,
            'form':form,
            'phongban':phongban,
        }
        return render(request,"giaichi/form_giai_chi_khac_moi.html",context)
    
    def post(self,request):
        
        
        file = request.FILES['filegiaichi']
        u = User.objects.get(username=request.user)
        id_pb =request.POST.get('phongbanguiduyet')
        p = Phongban.objects.get(pk=id_pb)
        nv = Nhanvien.objects.get(username = u)

       
        ghichu =request.POST.get('ghichu')
        gd = request.POST.get('guiduyet')
        if gd:
            if int(gd) == 0:
                tpd = False
                sd = False
            if int(gd) == 1:
                tpd = False
                sd= True  
        Giaichi.objects.create(
            dexuat=None,
            hangmuc=2,  
            trangthaiduyet_tp=tpd,
            trangthaiduyet_sep=sd,
             trangthaiduyet_tckt = True,
            trangthaiduyetgiaichi=False,
            trangthaihuy = False,
            trangthaihoanthanh =False,
            guiduyet=request.POST.get('guiduyet'),
            nhanvien=nv,
            phongban = p,
            username = request.user,
            giaichihanghoa=None,
            giaichithietbi = None,
            giaichikhac=request.POST.get('giaichihanghoa'),
            noidungdexuat=None,
            tieude=request.POST.get('tieude'),
            ghichu =ghichu,
            filegiaichi = file,
            tientamung = 0,
            tiengiaichi = request.POST.get('tiengiaichi'),
           
        )

        return render(request,"giaichi/tao_giai_chi.html")



class Giaichithietbi_moi(LoginRequiredMixin,View):
    login_url="login/"
    redirect_field_name = 'redirect_to'
    def get(self,request):
        user = request.user
        form = Formtaogiaichi_dx()
        nv = Nhanvien.objects.filter(username =user).first
        phongban = Phongban.objects.all()
        
        context ={
            'nhanvien':nv,
            'form':form,
            'phongban':phongban,
        }
        return render(request,"giaichi/form_giai_chi_thiet_bi_moi.html",context)
    
    def post(self,request):
        if request.method == "POST":
            sl1 =  int(request.POST.get('soluong_1'))
            sl2 =  int(request.POST.get('soluong_2'))
            sl3 =  int(request.POST.get('soluong_3'))
            sl4 =  int(request.POST.get('soluong_4'))
            sl5 =  int(request.POST.get('soluong_5'))
            dg1 =  int(request.POST.get('dongia_1'))
            dg2 =  int(request.POST.get('dongia_2'))
            dg3 =  int(request.POST.get('dongia_3'))
            dg4 =  int(request.POST.get('dongia_4'))
            dg5 =  int(request.POST.get('dongia_5'))
            tt1 =  sl1*dg1
            tt2 =  sl2*dg2
            tt3 =  sl3*dg3
            tt4 =  sl4*dg4
            tt5 =  sl5*dg5
            tiengiaichi = tt1+tt2+tt3+tt4+tt5
            gc = None
            file = request.FILES['filegiaichi']
            u = User.objects.get(username=request.user)
            id_pb =request.POST.get('phongbanguiduyet')
            p = Phongban.objects.get(pk=id_pb)
            nv = Nhanvien.objects.get(username = u)
            tgc = request.POST.get('tgc')
            ghichu =request.POST.get('ghichu')
            noidung = {
                        'hanghoa_1':request.POST.get('hanghoa_1'),
                        'soluong_1':request.POST.get('soluong_1'),
                        'dongia_1':request.POST.get('dongia_1'),
                        'thanhtien_1':tt1,
                        'hanghoa_2':request.POST.get('hanghoa_2'),
                        'soluong_2':request.POST.get('soluong_2'),
                        'dongia_2':request.POST.get('dongia_2'),
                        'thanhtien_2':tt2,
                        'hanghoa_3':request.POST.get('hanghoa_3'),
                        'soluong_3':request.POST.get('soluong_3'),
                        'dongia_3':request.POST.get('dongia_3'),
                        'thanhtien_3':tt3,
                        'hanghoa_4':request.POST.get('hanghoa_4'),
                        'soluong_4':request.POST.get('soluong_4'),
                        'dongia_4':request.POST.get('dongia_4'),
                        'thanhtien_4':tt4,
                        'hanghoa_5':request.POST.get('hanghoa_5'),
                        'soluong_5':request.POST.get('soluong_5'),
                        'dongia_5':request.POST.get('dongia_5'),
                        'thanhtien_5':tt5,
                    }
            gd = request.POST.get('guiduyet')
            if gd:
                if int(gd) == 0:
                    tpd = False
                    sd = False
                if int(gd) == 1:
                    tpd = False
                    sd= True  
            Giaichi.objects.create(
                dexuat=gc,
                trangthaiduyet_tp=tpd,
                trangthaiduyet_tckt = True,
                trangthaiduyet_sep=sd,
                trangthaiduyetgiaichi=False,
                trangthaihuy = False,
                trangthaihoanthanh =False,
                nhanvien=nv,
                hangmuc = 1,
                guiduyet = request.POST.get('guiduyet'),
                phongban = p,
                username = request.user,
                noidungdexuat=".",
                tieude=request.POST.get('tieude'),
                ghichu =ghichu,
                filegiaichi =file,
                tientamung = 0,
                tiengiaichi = tiengiaichi,
                giaichihanghoa=None,
                giaichithietbi = noidung,
                giaichikhac=None,
            )

            return render(request,"giaichi/tao_giai_chi.html")


class Giaichichuaduyet(LoginRequiredMixin,View):
    login_url="login/"
    redirect_field_name = 'redirect_to'
    def get(self,request):
        user = request.user
        gc = Giaichi.objects.filter(Q(trangthaiduyet_tp =False)|Q(trangthaiduyet_sep =False),
                                  username = user,trangthaihuy=False
                                  
                                  ).order_by('created_at','id')
        context ={
            
            'giaichi':gc,
        }
        

        return render(request,"giaichi/giai_chi_chua_duyet.html",context)
class Giaichidaduyet(LoginRequiredMixin,View):
    login_url="login/"
    redirect_field_name = 'redirect_to'
    def get(self,request):
        user = request.user
        gc = Giaichi.objects.filter(
                                  username = user,
                                  trangthaiduyet_tp =True,
                                  trangthaiduyet_tckt =True,
                                  trangthaiduyet_sep=True,
                                  trangthaiduyetgiaichi=True,
                                  trangthaihoanthanh=False
                                  ).order_by('created_at','id')
        context ={
            
            'giaichi':gc,
        }
        

        return render(request,"giaichi/giai_chi_da_duyet.html",context)
              
class Giaichidathanhtoan(LoginRequiredMixin,View):
    login_url="login/"
    redirect_field_name = 'redirect_to'
    def get(self,request):
        user = request.user
        gc = Giaichi.objects.filter(
                                  username = user,
                                  trangthaiduyet_tp =True,
                                  trangthaiduyet_tckt =True,
                                  trangthaiduyet_sep=True,
                                  trangthaihoanthanh=True,
                                  trangthaiduyetgiaichi=True,
                                  ).order_by('created_at','id')
        context ={
            
            'giaichi':gc,
        }
        

        return render(request,"giaichi/giai_chi_da_thanh_toan.html",context)
              
             
class Giaichidahuy(LoginRequiredMixin,View):
    login_url="login/"
    redirect_field_name = 'redirect_to'
    def get(self,request):
        user = request.user
        gc = Giaichi.objects.filter(
                                  username = user,
                                  trangthaihuy=True,
                                  ).order_by('created_at','id')
        context ={
            
            'giaichi':gc,
        }
        

        return render(request,"giaichi/giai_chi_da_huy.html",context)
          

class Quanlygiaichi(LoginRequiredMixin,View):
    login_url ="login/"
    redirect_field_name = 'redirect_to'
    def get(self,request):
        user  = request.user 
        nv = Nhanvien.objects.get(username = user)
        cv = Chucvu_Congviec.objects.filter(phongban=nv.phongban)
        for item in cv :
            if item.tencongviec == "TP":
                gc =Giaichi.objects.filter(
                                  trangthaiduyet_tp = False,
                                  trangthaihuy = False,
                                  
                                  phongban = nv.phongban,
                                  )

                context ={
                        'giaichi':gc,
                        }   
                return render(request,'giaichi/ql_giaichi_cho_xu_ly.html',context)
        return HttpResponse("Bạn Không Có Quyền :  <a href='javascript:history.back()' >Quay Lại</a>")

class Quanlygiaichi_tckt(LoginRequiredMixin,View):
    login_url = "login/"
    redirect_field_name = 'redirect_to'
    def get(self,request):
        user = request.user
        nhanvien = Nhanvien.objects.get(username =user )
        nvcv = Chucvu_Congviec.objects.get(nhanvien = nhanvien)
        gc =Giaichi.objects.filter(
                                  trangthaiduyet_tp = True,
                                  trangthaiduyet_tckt = False,
                                  
                                  trangthaihuy = False,
                                  )
        gctp =Giaichi.objects.filter(
                                  trangthaiduyet_tp = True,
                                  trangthaiduyet_tckt = False,
                                  phongban = nvcv.phongban,
                                  trangthaihuy = False,
                                  )
        context = {
            'giaichi':gc,
            'giaichitp':gctp,
        }
        return render(request,'giaichi/ql_giaichi_cho_xu_ly_tckt.html',context)

class Quanlygiaichi_sep(LoginRequiredMixin,View):
    login_url ="login/"
    redirect_field_name = 'redirect_to'
    def get(self,request):
        user = request.user
        nhanvien = Nhanvien.objects.get(username =user )
        nvcv = Chucvu_Congviec.objects.get(nhanvien = nhanvien)
        
        gc =Giaichi.objects.filter(
                                  trangthaiduyet_tp = True,
                                  trangthaiduyet_sep = False,
                                   trangthaiduyet_tckt = True,
                                  trangthaihuy = False,
                                  )
        gctp =Giaichi.objects.filter(
                                  trangthaiduyet_tp = True,
                                   trangthaiduyet_tckt = True,
                                  trangthaiduyet_sep = False,
                                  trangthaihuy = False,
                                  phongban = nvcv.phongban, 
                                  )
        phongban = Phongban.objects.all().exclude(tenpb="SEP")
        context ={
            'giaichi':gc,
            'phongban':phongban,
            'giaichi_tp':gctp,
        }
        return render(request,'giaichi/ql_giaichi_cho_xu_ly_sep.html',context)
class Quanlygiaichi_daduyet(LoginRequiredMixin,View):
    login_url ="login/"
    redirect_field_name = 'redirect_to'
    def get(self,request):
        user = request.user
        nhanvien = Nhanvien.objects.get(username =user )
        nvcv = Chucvu_Congviec.objects.get(nhanvien = nhanvien)
        gc =Giaichi.objects.filter(
                                  trangthaiduyet_tp = True,
                                   trangthaiduyet_sep = True,
                                  trangthaihuy = False,
                                  trangthaihoanthanh=False
                                  )
        gctp =Giaichi.objects.filter(
                                   trangthaiduyet_tp = True,
                                   trangthaiduyet_sep = True,
                                  trangthaihuy = False,
                                  trangthaihoanthanh=False,
                                   phongban = nvcv.phongban,
                                  )
                                  
        phongban = Phongban.objects.all()
        context ={
            'giaichi':gc,
            'giaichi_tp':gctp,
            'phongban':phongban,
        }
        return render(request,'giaichi/ql_giaichi_da_duyet.html',context)
class Quanlygiaichi_hoanthanh(LoginRequiredMixin,View):
    login_url ="login/"
    redirect_field_name = 'redirect_to'
    def get(self,request):
        user = request.user
        nhanvien = Nhanvien.objects.get(username =user )
        nvcv = Chucvu_Congviec.objects.get(nhanvien = nhanvien)
        gc =Giaichi.objects.filter(
                                  trangthaiduyet_tp = True,
                                   trangthaiduyet_sep = True,
                                  trangthaihuy = False,
                                  trangthaihoanthanh=True
                                  )
        gctp =Giaichi.objects.filter(
                                   trangthaiduyet_tp = True,
                                   trangthaiduyet_sep = True,
                                  trangthaihuy = False,
                                  trangthaihoanthanh=True,
                                   phongban = nvcv.phongban,
                                  )
                                  
        phongban = Phongban.objects.all().exclude(tenpb="SEP")
        context ={
            'giaichi':gc,
            'giaichi_tp':gctp,
            'phongban':phongban,
        }
        return render(request,'giaichi/ql_giaichi_da_hoan_thanh.html',context)

class Quanlygiaichi_dahuy(LoginRequiredMixin,View):
    login_url ="login/"
    redirect_field_name = 'redirect_to'
    def get(self,request):
        user = request.user
        nhanvien = Nhanvien.objects.get(username =user )
        nvcv = Chucvu_Congviec.objects.get(nhanvien = nhanvien)
        gc =Giaichi.objects.filter(
                                  trangthaihuy = True,
                                  )
        gctp =Giaichi.objects.filter(
                                  trangthaihuy = True,
                                  phongban = nvcv.phongban,
                                  )
        phongban = Phongban.objects.all().exclude(tenpb="SEP")
        context ={
            'giaichi':gc,
            'giaichi_tp':gctp,
            'phongban':phongban,
        }
        return render(request,'giaichi/ql_giaichi_da_huy.html',context)

class Xu_ly_giai_chi(LoginRequiredMixin,View):
    login_url ="/login/"
    redirect_field_name = 'redirect_to'
    def get(self,request,giaichi_id):
        user = request.user
        
        nhanvien = Nhanvien.objects.get(username = user)
        cv = Chucvu_Congviec.objects.get(nhanvien=nhanvien)
        if cv.tencongviec == "TP" :
            gc = Giaichi.objects.filter(pk=giaichi_id,trangthaiduyet_tp =False,trangthaihuy = False,phongban=nhanvien.phongban).first
            if gc:
                context = {
                    'giaichi':gc,
                    'nhanvien':nhanvien,
                
                }
            else:
                return HttpResponse("ERROR")
        

            return render(request,"giaichi/form_xu_ly_tp.html",context) 
        if cv.tencongviec == "SEP":
            gc = Giaichi.objects.filter(pk=giaichi_id,trangthaiduyet_tp = True,trangthaiduyet_sep=False).first
            if gc:
                context = {
                  'giaichi':gc,
                  'nhanvien':nhanvien,
               
              }
            else:
                return HttpResponse("ERROR")
        
            return render(request,"giaichi/form_xu_ly_sep.html",context) 


    def post(self,request,giaichi_id):
        
        user = request.user
        
        nhanvien = Nhanvien.objects.get(username = user)
        cv = Chucvu_Congviec.objects.get(nhanvien=nhanvien)
        gctp = Giaichi.objects.filter(pk=giaichi_id,trangthaiduyet_tp =False,trangthaiduyet_sep = False,trangthaihuy=False).first
        gcsep = Giaichi.objects.filter(pk=giaichi_id,trangthaiduyet_tp =True,trangthaiduyet_sep = False,trangthaihuy=False).first
        if gctp:   
            if cv.tencongviec == "TP":
                giaichi = Giaichi.objects.get(pk=giaichi_id)
                ttd = request.POST.get('pheduyet')
                if ttd == '0':

                    ttd_tp = True
                    tth = False
                    ttd = True

                if ttd == '1':

                    ttd_tp = False
                    tth = True
                    ttd = True
                if giaichi.hangmuc == '0':
                    tckt = False
                if giaichi.hangmuc == '1':
                    tckt = True
                if giaichi.hangmuc == '2':
                    tckt = True
                csrf = request.POST.get('csrfmiddlewaretoken')
                querydict = QueryDict("",mutable=True)
                querydict.update(
                        {
                            'csrfmiddlewaretoken':csrf,
                            'trangthaiduyet_tp':ttd_tp,
                            'trangthaiduyet_tckt':tckt,
                            'trangthaihuy':tth ,

                            'trangthaiduyetgiaichi':ttd,
                        }
                    )
                form =  Formxuly_giaichi_tp(querydict,instance=giaichi)
                if form.is_valid():
                    form.save()
                return redirect('quan-ly-giai-chi-tp')
        else:
            return HttpResponse("ERROR")
        if gcsep:   
            if cv.tencongviec == "SEP":
                giaichi = Giaichi.objects.get(pk=giaichi_id)
                ttd = request.POST.get('pheduyet')
                if ttd == '0':
                    ttd_sep = True
                    tth = False
                    ttd = True
                if ttd == '1':

                    ttd_sep = False
                    tth = True
                    ttd = True

                csrf = request.POST.get('csrfmiddlewaretoken')
                querydict = QueryDict("",mutable=True)
                querydict.update(
                        {
                            'csrfmiddlewaretoken':csrf,
                            'trangthaiduyet_sep':ttd_sep,
                            'trangthaihuy':tth ,
                            'trangthaiduyetgiaichi':ttd,
                        }
                    )
                form =  Formxuly_giaichi_sep(querydict,instance=giaichi)
                if form.is_valid():
                    form.save()
                return redirect('quan-ly-giai-chi-sep')
        else:
            return HttpResponse("ERROR")


class Xu_ly_giai_chi_tckt(LoginRequiredMixin,View):
    login_url ="/login/"
    redirect_field_name = 'redirect_to'
    def get(self,request,giaichi_id):
        if request.user.username  == "thangnguyen":
            gc = Giaichi.objects.get(pk=giaichi_id)
            context = {
                'giaichi':gc,
            }
            return render(request,'giaichi/form_xu_ly_tckt.html',context)
        return HttpResponse("Bạn Không Có Quyền - Chỉ TP Tài Chính Kế Toán mới có thê thao tác")
        
    def post(self,request,giaichi_id):

        if request.user.username  == "thangnguyen":
            
            giaichi = Giaichi.objects.get(pk=giaichi_id)
            ttd = request.POST.get('pheduyet')
            if ttd == '0':
                tckt = True
                tth = False
                ttd = True
            if ttd == '1':

                tckt = False
                tth = True
                ttd = True

            csrf = request.POST.get('csrfmiddlewaretoken')
            querydict = QueryDict("",mutable=True)
            querydict.update(
                        {
                            'csrfmiddlewaretoken':csrf,
                            'trangthaiduyet_tckt':tckt,
                            'trangthaihuy':tth ,
                            'trangthaiduyetgiaichi':ttd,
                        }
                    )
            form =  Formxuly_giaichi_tckt(querydict,instance=giaichi)
            if form.is_valid():
                form.save()
                return redirect('quan-ly-giai-chi-tckt')
            

        return HttpResponse("Bạn Không Có Quyền - Chỉ TP Tài Chính Kế Toán mới có thê thao tác")



class View_giaichi(LoginRequiredMixin,View):
    login_url="login/"
    redirect_field_name = 'redirect_to'
    def get(self,request,giaichi_id):
        user = request.user
        gc = Giaichi.objects.get(pk=giaichi_id)
        nhanvien = Nhanvien.objects.get(username = user )
        nvcv = Chucvu_Congviec.objects.get(nhanvien = nhanvien)
        
        if user == gc.username or nvcv.tencongviec =="SEP" or user.username == 'thangnguyen':# or str(user) == 'thangnguyen': 
            context = {
                    'giaichi':gc
                }
            return render(request,"giaichi/view_giai_chi.html",context)

        else:
            return HttpResponse("Bạn Không Có Quyền :  <a href='javascript:history.back()' >Quay Lại</a>")
        
class View_giaichi_tp(LoginRequiredMixin,View):
     
    def get(self,request,giaichi_id):
        user = request.user
        nhanvien = Nhanvien.objects.get(username = user )
        nvcv = Chucvu_Congviec.objects.get(nhanvien = nhanvien)
        gctp = Giaichi.objects.get(pk=giaichi_id)
        if nvcv.tencongviec == "TP" and nvcv.phongban == gctp.phongban :
            context ={
                'giaichi_tp':gctp,
            }
            return render(request,"giaichi/view_giai_chi.html",context)
        else:
            return HttpResponse("Bạn Không Có Quyền :  <a href='javascript:history.back()' >Quay Lại</a>")





class Edit_giaichi(LoginRequiredMixin,View):
    login_url="login/"
    redirect_field_name = 'redirect_to'
    def get(self,request,giaichi_id):
        user = request.user
        gc = Giaichi.objects.get(pk=giaichi_id)
        phongban = Phongban.objects.exclude(Q(tenpb="SEP")|Q(tenpb=gc.phongban.tenpb))
        
        form = Form_edit_giai_chi(instance=gc)
       
        if user == gc.username and gc.trangthaihoanthanh == False:
            context ={
                'phongban':phongban,
                'giaichi':gc,
                'form':form,
                
            }
            return render(request,"giaichi/edit_giai_chi.html",context)

        else:
            return HttpResponse("Bạn Không Có Quyền :  <a href='javascript:history.back()' >Quay Lại</a>")
    def post(self,request,giaichi_id):
       
        gc = Giaichi.objects.get(pk=giaichi_id)
        
        if request.user == gc.username:
            csrf = request.POST.get('csrfmiddlewaretoken')

            u = User.objects.get(username=request.user)
            nv = Nhanvien.objects.get(username = u)
                
            id_pb =request.POST.get('phongbanguiduyet')
            p = Phongban.objects.get(pk=id_pb)
            ghichu =request.POST.get('ghichu')
            gd = request.POST.get('guiduyet')
            if gd:
                if int(gd) == 0:
                    tpd = False
                    sd = False
                if int(gd) == 1:
                    tpd = False
                    sd= True
            if gc.hangmuc == "1":
                sl1 =  int(request.POST.get('soluong_1'))
                sl2 =  int(request.POST.get('soluong_2'))
                sl3 =  int(request.POST.get('soluong_3'))
                sl4 =  int(request.POST.get('soluong_4'))
                sl5 =  int(request.POST.get('soluong_5'))
                dg1 =  int(request.POST.get('dongia_1'))
                dg2 =  int(request.POST.get('dongia_2'))
                dg3 =  int(request.POST.get('dongia_3'))
                dg4 =  int(request.POST.get('dongia_4'))
                dg5 =  int(request.POST.get('dongia_5'))
                tt1 =  sl1*dg1
                tt2 =  sl2*dg2
                tt3 =  sl3*dg3
                tt4 =  sl4*dg4
                tt5 =  sl5*dg5
                tiengiaichi = tt1+tt2+tt3+tt4+tt5
                noidung = {
                            'hanghoa_1':request.POST.get('hanghoa_1'),
                            'soluong_1':request.POST.get('soluong_1'),
                            'dongia_1':request.POST.get('dongia_1'),
                            'thanhtien_1':tt1,
                            'hanghoa_2':request.POST.get('hanghoa_2'),
                            'soluong_2':request.POST.get('soluong_2'),
                            'dongia_2':request.POST.get('dongia_2'),
                            'thanhtien_2':tt2,
                            'hanghoa_3':request.POST.get('hanghoa_3'),
                            'soluong_3':request.POST.get('soluong_3'),
                            'dongia_3':request.POST.get('dongia_3'),
                            'thanhtien_3':tt3,
                            'hanghoa_4':request.POST.get('hanghoa_4'),
                            'soluong_4':request.POST.get('soluong_4'),
                            'dongia_4':request.POST.get('dongia_4'),
                            'thanhtien_4':tt4,
                            'hanghoa_5':request.POST.get('hanghoa_5'),
                            'soluong_5':request.POST.get('soluong_5'),
                            'dongia_5':request.POST.get('dongia_5'),
                            'thanhtien_5':tt5,
                        }
                
                querydict = QueryDict("",mutable=True)

                querydict.update({
                                'csrfmiddlewaretoken':csrf,
                                'tieude':request.POST.get('tieude'),
                                'phongban':p,
                                'guiduyet':gd,
                                'trangthaiduyet_tp':tpd,
                                'trangthaiduyet_sep':sd,
                                'tiengiaichi':tiengiaichi,
                                'giaichithietbi':noidung,
                                'ghichu':ghichu,
                                'giaichihanghoa':gc.giaichihanghoa,
                                'giaichikhac':gc.giaichikhac,
                                'filegiaichi':request.POST.get('filegiaichi')
                                })
                form = Form_edit_giai_chi(querydict,request.FILES,instance=gc)
                if form.is_valid():
                    form.save()
                    messages.success(request,"Cập Nhật Thành Công Giải Chi "+gc.tieude)
                else:
                    return HttpResponse("Cập Nhật Lỗi Không Mong Muốn :   <a href='javascript:history.back()' >Quay Lại</a>")
            if gc.hangmuc == "0":
                querydict = QueryDict("",mutable=True)

                querydict.update({
                                'csrfmiddlewaretoken':csrf,
                                'tieude':request.POST.get('tieude'),
                                'phongban':p,
                                'guiduyet':gd,
                                'trangthaiduyet_tp':tpd,
                                'trangthaiduyet_sep':sd,
                                'tiengiaichi':request.POST.get('tiengiaichi'),
                                'giaichithietbi':gc.giaichithietbi,
                                'ghichu':ghichu,
                                'giaichihanghoa':request.POST.get('giaichihanghoa'),
                                'giaichikhac':gc.giaichikhac,
                                'filegiaichi':request.POST.get('filegiaichi')
                                })
                form = Form_edit_giai_chi(querydict,request.FILES,instance=gc)
                if form.is_valid():
                    form.save()
                    messages.success(request,"Cập Nhật Thành Công Giải Chi "+gc.tieude)
                    return redirect("giai-chi-chua-duyet")
                else:return HttpResponse("Lỗi Không Mong Muốn :   <a href='javascript:history.back()' >Quay Lại</a>")
                    
            if gc.hangmuc == "2":
                querydict = QueryDict("",mutable=True)

                querydict.update({
                                'csrfmiddlewaretoken':csrf,
                                'tieude':request.POST.get('tieude'),
                                'phongban':p,
                                'guiduyet':gd,
                                'trangthaiduyet_tp':tpd,
                                'trangthaiduyet_sep':sd,
                                'tiengiaichi':request.POST.get('tiengiaichi'),
                                'giaichithietbi':gc.giaichithietbi,
                                'ghichu':ghichu,
                                'giaichihanghoa':gc.giaichihanghoa,
                                'giaichikhac':request.POST.get('giaichikhac'),
                                'filegiaichi':request.POST.get('filegiaichi')
                                })
                form = Form_edit_giai_chi(querydict,request.FILES,instance=gc)
                if form.is_valid():
                    form.save()
                    messages.success(request,"Cập Nhật Thành Công Giải Chi "+gc.tieude)
                    return redirect("giai-chi-chua-duyet")
                else:return HttpResponse("Lỗi Không Mong Muốn :   <a href='javascript:history.back()' >Quay Lại</a>")
                    

            return redirect("giai-chi-chua-duyet")
        else:
            return HttpResponse("Lỗi Không Mong Muốn :   <a href='javascript:history.back()' >Quay Lại</a>")


class Thanhtoan_giaichi(LoginRequiredMixin,View):
    login_url="login/"
    redirect_field_name = 'redirect_to'
    def get(self,request):
        user = request.user
        nhanvien = Nhanvien.objects.get(username = user )
        nvcv = Chucvu_Congviec.objects.get(nhanvien = nhanvien)
        
        if nvcv.tencongviec == "THU QUY": 
            gc_ctt = Giaichi.objects.filter(trangthaiduyetgiaichi =True,trangthaiduyet_tp=True,trangthaiduyet_sep=True,trangthaihoanthanh=False,trangthaihuy=False).order_by('-id')
            gc_dtt = Giaichi.objects.filter(trangthaiduyetgiaichi =True,trangthaiduyet_tp=True,trangthaiduyet_sep=True,trangthaihoanthanh=True,trangthaihuy=False)
        
            context= {
                'giaichi_ctt':gc_ctt,
                'giaichi_dtt':gc_dtt,
                }
            return render(request,"thuquy/thanh-toan-giai-chi.html",context)
        else:
            return HttpResponse("Bạn Không Đủ Quyền Làm Việc Này")

class Xacnhanthanhtoan_giaichi(LoginRequiredMixin,View):
    login_url="login/"
    redirect_field_name = 'redirect_to'
    def get(self,request,giaichi_id):
        user = request.user
        nhanvien = Nhanvien.objects.get(username = user )
        nvcv = Chucvu_Congviec.objects.get(nhanvien = nhanvien)
        
        if nvcv.tencongviec == "THU QUY": 
            gc= Giaichi.objects.get(pk=giaichi_id)
            form = Form_nhap_giai_chi(instance=gc)
            context= {
                'giaichi':gc,
                'form':form,
                }
            return render(request,"thuquy/form_nhap_thanh_toan_giai_chi.html",context)
        else:
            return HttpResponse("Bạn Không Đủ Quyền Làm Việc Này")

    def post(self,request,giaichi_id):
        if request.POST:
            user = request.user
            nhanvien = Nhanvien.objects.get(username = user )
            nvcv = Chucvu_Congviec.objects.get(nhanvien = nhanvien)
            if nvcv.tencongviec == "THU QUY": 
                gc= Giaichi.objects.get(pk=giaichi_id)
                querydict = QueryDict("",mutable=True)
                csrf = request.POST.get('csrfmiddlewaretoken')
                querydict.update({
                    'csrfmiddlewaretoken':csrf,
                    'trangthaihoanthanh':True,
                    'noidungthanhtoan':request.POST.get('noidungthanhtoan')
                })
                form = Form_nhap_giai_chi(querydict,instance=gc)
                if form.is_valid():
                    form.save()
                    return redirect('thanh-toan-giai-chi')
                else:
                    return Http404()
                
                
            else:
                return HttpResponse("Bạn Không Đủ Quyền Làm Việc Này")
        else:
            return Http404()


class Baocaogiaichi(LoginRequiredMixin,View):
    login_url = "login/"
    redirect_field_name = 'redirect_to'
    def get(self,request):
        gctp = 0
        print(request.POST)
        phongban = Phongban.objects.all().exclude(tenpb='SEP')
        context={
            'giaichitp':gctp,
            'phongban':phongban,
        }
        return render(request,"giaichi/baocao.html",context)
class Loadgiaichi(View):

    def get(self,request):
        pb = request.GET.get('pb')
        thang = request.GET.get('thang')
        nam = request.GET.get('nam')
        if pb=="0":
            if thang == '0':
                giaichi = Giaichi.objects.filter(trangthaihoanthanh=True,created_at__year=nam).order_by('-id')
            else:
                giaichi =Giaichi.objects.filter(trangthaihoanthanh=True,created_at__year=nam,created_at__month=thang).order_by('-id')
        else:
            phongban_gc = Phongban.objects.get(pk=pb)
            if thang == '0':
                giaichi = Giaichi.objects.filter(phongban = phongban_gc ,trangthaihoanthanh=True,created_at__year=nam).order_by('-id')
            else:
                giaichi = Giaichi.objects.filter(phongban = phongban_gc ,trangthaihoanthanh=True ,created_at__year=nam,created_at__month=thang).order_by('id')
        context = {
            'giaichi':giaichi,
        }
        return render(request,'giaichi/load_bao_cao.html',context)