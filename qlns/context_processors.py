from django.http import request
from django.http.response import HttpResponse
from qlns.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

def dexuat_extra(request):
    user = request.user.is_authenticated
    if user:
        
        dexuat_chua_duyet  = Dexuat.objects.filter(Q(trangthaiduyet_tp=False)|Q(trangthaiduyet_sep=False),tinhtranghuy=False,username=request.user)
        dexuat_da_duyet = Dexuat.objects.filter(username=request.user,trangthaiduyet_tp=True,trangthaiduyet_sep=True,tinhtranghuy=False)
        dexuat_huy = Dexuat.objects.filter(username=request.user,tinhtranghuy=True)
        dem_cd  =  0
        dem_dd  =  0 
        dem_huy =  0
        if dexuat_chua_duyet :
            
            for item in dexuat_chua_duyet:
                dem_cd +=1
        if dexuat_da_duyet :
            
            for item in dexuat_da_duyet:
                dem_dd +=1
        if dexuat_huy :
            for item in dexuat_huy:
                dem_huy +=1
        context = {
                    'dem_cd':dem_cd,
                    'dem_dd':dem_dd,
                    'dem_huy':dem_huy,

                }
        return {'context':context}
    else:
        dem_cd=0
        dem_dd=0
        dem_huy=0
        context = {
                    'dem_cd':dem_cd,
                    'dem_dd':dem_dd,
                    'dem_huy':dem_huy,

                }
        return {'context':context}



def nhanvienindex(request):
    user = request.user.is_authenticated
    if user:
        
        nv = Nhanvien.objects.get(username=request.user)   
        tennv=""
        if nv:
            tennv = nv.tennv
        context ={
                'tennv':tennv,
                }
        return {'nhanvien':context}
    else:
        tennv = "Khách"
        context ={
                'tennv':tennv,
                }
        return {'nhanvien':context}

def Dexuat_total(request):
    user = request.user.is_authenticated
    if user:
        nv = Nhanvien.objects.get(username=request.user)
        demtp=0
        demsep=0
        demht=0
        demtu=0
        demhuy = 0
        dem_ht_tp = 0
        dem_tu_tp = 0
        dem_huy_tp = 0
        dem_dx_gc_tp = 0
        dem_dx_gc_sep = 0
        if nv:
            cv = Chucvu_Congviec.objects.get(nhanvien=nv)
            if cv:
                if cv.tencongviec == "TP":
                    dxht_tp = Dexuat.objects.filter(phongban = nv.phongban,trangthaiduyet_sep = True,trangthaiduyet_tp=True)
                    for item in dxht_tp:
                        dem_ht_tp+=1
                    dxtu_tp = Dexuat.objects.filter(phongban = nv.phongban,
                                  trangthaiduyet_tp = True,
                                  trangthaiduyet_sep = True,
                                  tinhtrangtamung=True,
                                  tinhtranghuy = False,
                                  ).exclude(tientamung=0)
                    for item in dxtu_tp:
                        dem_tu_tp+=1
                    dxhuy_tp = Dexuat.objects.filter(tinhtranghuy=True)
                    for item in dxhuy_tp:
                        dem_huy_tp += 1
                    

                else:
                    dem_ht_tp = 0
                    dem_tu_tp = 0
                    dem_huy_tp =0
            else:
                dem_ht_tp = 0
                dem_tu_tp = 0
                dem_huy_tp =0
        else:
            dem_ht_tp = 0
            dem_tu_tp = 0
        
        pb = Dexuat.objects.filter(phongban = nv.phongban,trangthaiduyet_tp=False)
        if pb:
            for item in pb:
                demtp += 1
        else:
            demtp=0
        
        
        dxs = Dexuat.objects.filter(trangthaiduyet_sep = False,trangthaiduyet_tp=True,tinhtranghuy=False)
        if dxs:
            for item in dxs:
                demsep+=1
        else:
            demsep = 0
        
        dxht = Dexuat.objects.filter(trangthaiduyet_sep = True,trangthaiduyet_tp=True)
        if dxht:
            for item in dxht:
                demht+=1
        else:
            demht=0
        
        
        dxtu = Dexuat.objects.filter( trangthaiduyet_tp = True,
                                  trangthaiduyet_sep = True,
                                  tinhtrangtamung=True,
                                  tinhtranghuy = False,
                                  ).exclude(tientamung=0)
        if dxtu:
                for item in dxtu:
                    demtu+=1
        else:
            demtu=0
        dxhuy = Dexuat.objects.filter(tinhtranghuy=True)
        if dxhuy:
            for item in dxhuy:
                demhuy+=1
        else:
            demhuy=0
        
        context = {
                 'demht_tp':dem_ht_tp,  
                 'demtu_tp':dem_tu_tp,
                 'demhuy_tp':dem_huy_tp,
                 'demtp':demtp,
                 'demsep':demsep,
                 'demht':demht,
                 'demtu':demtu,
                 'demhuy':demhuy,
                }
        return {'duyet_tp':context}
    else:
        context = {
                 'demht_tp':0,
                 'demtu_tp':0,
                 'demhuy_tp':0,
                 'demtp':0,
                 'demsep':0,
                 'demht':0,
                 'demtu':0,
                 'demhuy':0,
                }
        return {'duyet_tp':context}
def Tamung(request):
    user = request.user.is_authenticated
    if user:
        dem_tamung_cn = 0 
        dem_tamung_dn = 0
        
        tamung_cn = Dexuat.objects.filter(trangthaiduyet_sep=True,trangthaiduyet_tp=True, tinhtranggiaichi = False,tientamung = 0)
        if tamung_cn:
            for item in tamung_cn:
                dem_tamung_cn+=1
        else:
            dem_tamung_cn =0
        
        tamung_dn = Dexuat.objects.filter(trangthaiduyet_sep=True,trangthaiduyet_tp=True,tinhtranggiaichi = False,).exclude(tientamung=0)
        if tamung_dn:
            for item in tamung_dn:
                dem_tamung_dn+=1
        else:
            dem_tamung_dn = 0

        context ={
            'dem_tamung_cn':dem_tamung_cn,
            'dem_tamung_dn':dem_tamung_dn,
        }
        return {'tamung':context}
    else:
        context ={
            'dem_tamung_cn':0,
            'dem_tamung_dn':0,
        }
        return {'tamung':context}


def sep(request):
    usercheck = request.user.is_authenticated
    if usercheck:
        sep =  False
        tp  =  False 
        ql  =  False
        tq  =  False 
        user = request.user
        nv = Nhanvien.objects.get(username = user)
        pq = Phanquyen.objects.all()
        if nv:
            cv = Chucvu_Congviec.objects.get(nhanvien=nv)
            if cv:
                if cv.tencongviec =="SEP":
                    sep = True
                if cv.tencongviec =="THU QUY":
                    tq = True
                if cv.tencongviec =="TP":
                    tp = True
                if sep == True and tp ==True:
                    ql = True
                context = {
                            'sep':sep,
                            'tp':tp,
                            'ql':ql,
                            'tq':tq,
                            'pq':pq
                         }
            else:
                context={
                            'sep':False,
                            'tp':False,
                            'ql':False,
                            'tq':False,

                          }
        else:
            context={
                'sep':False,
                'tp':False,
                'ql':False,
                'tq':False,
            }
    else:
            context={
                'sep':False,
                'tp':False,
                'ql':False,
                'tq':False,

            }

    return {'cv':context}


def giaichi_chuaduyet(request):
    usercheck = request.user.is_authenticated
    if usercheck:
        dem_gc_cd = 0
        dem_gc_dd = 0
        dem_sep_huy_tp = 0 # giai chi nhan vien bi huy
        dem_sep_cd = 0 
        dem_sep_dd = 0
        dem_sep_huy = 0
        dem_gc_hh = 0
        dem_gc_huy =0
        dem_tp_cd = 0
        dem_tp_dd= 0
        dem_tp_hh= 0
        dem_sep_cd_pb = 0
        dem_sep_hh = 0
        dem_tckt = 0
        dem_tp_tckt=0
        dem_sep_tckt=0
        gc_cd = Giaichi.objects.filter(Q(trangthaiduyet_tp =False)|Q(trangthaiduyet_sep =False),trangthaihuy=False,
                                  username = request.user,)
        gc_dd = Giaichi.objects.filter(username  = request.user,trangthaiduyetgiaichi=True,trangthaihoanthanh=False,trangthaiduyet_tp=True,trangthaiduyet_sep=True)
        gc_hh = Giaichi.objects.filter(username  = request.user,trangthaiduyetgiaichi=True,trangthaihoanthanh=True,trangthaiduyet_tp=True,trangthaiduyet_sep=True,trangthaihuy=False)
        nv = Nhanvien.objects.get(username =request.user)
        gc_huy = Giaichi.objects.filter(trangthaihuy =True ,username = request.user)
        nvcv = Chucvu_Congviec.objects.get(nhanvien=nv)
        gc_tckt =Giaichi.objects.filter(hangmuc="0",trangthaiduyet_tckt=False ,trangthaiduyet_tp=True ,trangthaihoanthanh=False ,trangthaihuy=False)
        
        if gc_tckt:
            for item in gc_tckt:
                dem_tckt+=1
        else:
            dem_tckt=0

        if gc_huy:
            for item in gc_huy:
                dem_gc_huy +=1
        else:
            dem_gc_huy =0 
        if gc_hh:
            for item in gc_hh:
                dem_gc_hh +=1
        else:
            dem_gc_hh =0

        if gc_cd:
            for item in gc_cd:
                dem_gc_cd +=1
        else:
            dem_gc_cd =0
        
        if gc_dd:
            for item in gc_dd:
                dem_gc_dd +=1
        else:
            dem_gc_dd = 0
        
        if nvcv.tencongviec=="TP":

            gc_tp_cd = Giaichi.objects.filter(trangthaiduyet_tp=False,phongban=nvcv.phongban,trangthaihuy=False) 
            gc_tp_dd = Giaichi.objects.filter(trangthaiduyet_tp=True,trangthaiduyet_sep=True,phongban=nvcv.phongban,trangthaihuy=False,trangthaihoanthanh=False) 
            gc_sep_cd_pb = Giaichi.objects.filter(trangthaiduyet_tp=True,trangthaiduyet_tckt = True,trangthaiduyet_sep=False,phongban=nvcv.phongban,trangthaihuy=False) 
            gc_tp_huy =Giaichi.objects.filter(trangthaihuy = True,phongban=nvcv.phongban) 
            gc_tp_hh = Giaichi.objects.filter(trangthaiduyet_tp=True,trangthaiduyet_sep=True,phongban=nvcv.phongban,trangthaihoanthanh=True,trangthaihuy=False) 
            gc_tp_tckt = Giaichi.objects.filter(hangmuc="0",trangthaiduyet_tp=True,trangthaiduyet_tckt=False,phongban=nvcv.phongban,trangthaihuy=False) 
            
            if gc_tp_tckt:
                for item in gc_tp_tckt:
                     dem_tp_tckt+=1
            else:

                dem_tp_tckt = 0
           
            if gc_tp_hh:
                for item in gc_tp_hh:
                     dem_tp_hh+=1
            else:

                dem_tp_hh = 0
            if gc_tp_huy:
                for item in gc_tp_huy:
                    dem_sep_huy_tp +=1
            else:
                dem_sep_huy_tp = 0
            if gc_sep_cd_pb:
                for item in gc_sep_cd_pb:
                    dem_sep_cd_pb+=1
            else:
                dem_sep_cd_pb = 0
            if gc_tp_cd:
                for item in gc_tp_cd:
                    dem_tp_cd+=1
            else:
                dem_tp_cd=0
            if gc_tp_dd:
                for item in gc_tp_dd:
                    dem_tp_dd+=1
            else:
                dem_gc_dd = 0
                dem_tp_dd = 0
        else:
            dem_tp_hh=0
            dem_tp_cd = 0
            dem_tp_dd = 0
            dem_sep_cd_pb = 0
            dem_sep_huy = 0
            dem_sep_huy_tp = 0
            dem_tckt =0
        if nvcv.tencongviec == "SEP":
            gc_sep_huy =Giaichi.objects.filter(trangthaihuy = True) 
            gc_sep_cd = Giaichi.objects.filter(trangthaiduyet_tp=True,trangthaiduyet_tckt = True,trangthaiduyet_sep=False,trangthaihuy=False) 
            gc_sep_dd = Giaichi.objects.filter(trangthaiduyet_tp=True,trangthaiduyet_sep=True,trangthaihuy=False,trangthaihoanthanh=False) 
            gc_sep_hh = Giaichi.objects.filter(trangthaiduyet_tp=True,trangthaiduyet_sep=True,trangthaihoanthanh=True,trangthaihuy=False) 
            gc_tckt =Giaichi.objects.filter(hangmuc="0",trangthaiduyet_tckt=False ,trangthaiduyet_tp=True ,trangthaihoanthanh=False ,trangthaihuy=False)
            
            if gc_tckt:
                for item in gc_tckt:
                    dem_sep_tckt +=1
            else:
                dem_sep_tckt = 0
            
            if gc_sep_hh:
                for item in gc_sep_hh:
                    dem_sep_hh +=1
            if gc_sep_huy:
                for item in gc_sep_huy:
                    dem_sep_huy +=1
            else:
                dem_sep_huy = 0
            if gc_sep_cd:
                for item in gc_sep_cd:
                    dem_sep_cd+=1
            else:
                dem_sep_cd=0

            if gc_sep_dd:
                for item in gc_sep_dd:
                    dem_sep_dd+=1
            else:
                dem_sep_dd = 0
        else:
            dem_sep_cd = 0
            dem_sep_dd = 0
            dem_sep_huy = 0
            
        
        
        context = {
            'gchuynv':dem_gc_huy,
            'gchhnv':dem_gc_hh,
            'gccdnv' : dem_gc_cd,
            'gcddnv' : dem_gc_dd,
            'gccdtp' : dem_tp_cd,
            'gchhtp':dem_tp_hh,
            'gccdsep': dem_sep_cd,
            'gcddtp' : dem_tp_dd,
            'gcddsep': dem_sep_dd,
            'gccdsep_pb':dem_sep_cd_pb,
            'gchuysep':dem_sep_huy,
            'gctphuy':dem_sep_huy_tp,
            'gchhsep':dem_sep_hh,
            'gctckt':dem_tckt,
            'gctptckt':dem_tp_tckt,
            'gcseptckt':dem_sep_tckt,
            
        }
    else:
        context = {
            'gchuynv' :0, 
            'gchhnv' : 0,
            'gccdnv' : 0,
            'gcddnv' : 0,
            'gccdtp' : 0,
            'gccdsep': 0,
            'gcddtp' : 0,
            'gcddsep': 0,
            'gctphuy':0,
            'gchhtp':0,
            'gchhsep':0,
            'gctckt':0,
            'gctptckt':0,
            'gcseptckt':0



        }
    return {'gc_nv':context}

    