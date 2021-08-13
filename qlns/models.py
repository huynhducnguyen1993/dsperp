
from django.contrib.auth import *
from django.db import models
from django.contrib import admin
from django.db.models.fields.related import OneToOneField
from django.utils.html import format_html
from django.contrib.auth.models import AbstractUser,User
from ckeditor.fields import *
from ckeditor_uploader.fields import *


class Phongban(models.Model):
    tenpb = models.CharField(default='',unique=True,max_length=255,verbose_name='Tên Phòng Ban')
    ngaythanhlap = models.DateTimeField(verbose_name='Năm thành lập',null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        verbose_name = "PHÒNG BAN"
        verbose_name_plural = 'PHÒNG BAN'

    def __str__(self):
        return self.tenpb

class Nhanvien(models.Model):
    manv = models.CharField(default='',unique=True,max_length=255,verbose_name='Mã Nhân Viên')
    username = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='Tài Khoản Nhân Viên')
    tennv = models.CharField(default='', max_length=255, verbose_name='Họ Tên Nhân Viên')
    gioitinh = models.BooleanField(default='',verbose_name='Check - Nếu là nam')
    ngaysinh =models.DateField(verbose_name='Ngày Sinh')
    diachi = models.CharField(default='', max_length=255, verbose_name='Địa chỉ thường trú')
    quequan =models.CharField(default='', max_length=255, verbose_name='Quê Quán')
    cmnd = models.CharField(default='', max_length=12, verbose_name='CCID')
    cmnd_1 =models.ImageField(default='',null=True, blank=True,upload_to='img/', verbose_name='Ảnh mặt trước CCID')
    cmnd_2 =models.ImageField(default='',null=True, blank=True, upload_to='img/', verbose_name='Ảnh mặt sau CCID')
    avatar = models.ImageField(default='',null=True, blank=True, upload_to='img/', verbose_name='Ảnh chân dung')
    sdt = models.CharField(default='', unique=True, max_length=255, verbose_name='Số Điện Thoại')
    line= models.CharField(default='', max_length=255, verbose_name='Line nội bộ')
    email =models.CharField(default='',unique=True, null=True,blank=True ,max_length=255, verbose_name='Email')
    phongban = models.ForeignKey(Phongban,default='',null=True,blank=True,on_delete=models.CASCADE)
    tinhtrangcongviec = models.BooleanField(default='1',verbose_name='Check --- (nếu nhân viên chính thức) ')
    chuky1 =models.FileField(blank=True,null=True,verbose_name='Upload chữ ký 1 ')
    chuky2 = models.FileField(blank=True, null=True, verbose_name='Upload chữ ký 2 ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "NHÂN VIÊN"
        verbose_name_plural = 'NHÂN VIÊN'


    def __str__(self):
        return self.tennv
class Chucvu_Congviec(models.Model):

    nhanvien = models.ForeignKey(Nhanvien ,on_delete=models.CASCADE,verbose_name='Nhân Viên')
    phongban = models.ForeignKey(Phongban,on_delete=models.CASCADE,verbose_name='Phòng ban')
    tencongviec = models.CharField(default='', max_length=255, verbose_name='Tên Công việc+ Chúc Vụ')
    motacongviec = models.TextField(verbose_name='Mô tả công việc')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "NHÂN VIÊN CHỨC VỤ"
        verbose_name_plural = 'NHÂN VIÊN CHỨC VỤ'

    def __int__(self):
        return self.nhanvien

class Baohiemyte(models.Model):
    nhanvien =models.OneToOneField(Nhanvien, on_delete=models.CASCADE)
    masobhyt = models.CharField(default='', unique=True, max_length=255, verbose_name='Mã Số BHXH')
    ngaythamgia = models.DateField(verbose_name='Ngày tham gia')
    noidangky = models.CharField(default='', max_length=255, verbose_name='Nơi đăng ký BHYT')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "BẢO HIỂM Y TẾ"
        verbose_name_plural = 'BẢO HIỂM Y TẾ'
    def __str__(self):
        return self.masobhyt

class Baohiemxahoi(models.Model):
    nhanvien = models.OneToOneField(Nhanvien, on_delete=models.CASCADE)
    masobhxh = models.CharField(unique=True,max_length=255,verbose_name='Mã Số BHXH')
    ngaythamgia =  models.DateField(verbose_name='Ngày tham gia')
    noidangky = models.CharField(default='', max_length=255, verbose_name='Địa chỉ đăng ký')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "BẢO HIỂM XÃ HỘI"
        verbose_name_plural = 'BẢO HIỂM XÃ HỘI'
    def __str__(self):
        return self.masobhxh

class Quatrinhdongbhxh(models.Model):
    tennhanvien = models.ForeignKey(Nhanvien,on_delete=models.CASCADE,verbose_name='Nhân Viên Đóng BHXH')
    thoigiandong = models.DateTimeField(verbose_name='Ngày-Tháng-Năm Đóng')
    sotiendong   = models.CharField(default='',max_length=255,verbose_name='Số Tiền Đóng BHXH')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "QUÁ TRÌNH ĐÓNG BẢO HIỂM XÃ HỘI"
        verbose_name_plural = "QUÁ TRÌNH ĐÓNG BẢO HIỂM XÃ HỘI"
    def __int__(self):
        return self.tennhanvien


class Hosonhanvien(models.Model):
    nhanvien = models.OneToOneField(Nhanvien, on_delete=models.CASCADE,verbose_name='Họ Tên Nhân Viên')
    masobh = models.CharField(unique=True,max_length=255,verbose_name='Mã Số HDLD ')
    ngaythuviec =  models.DateField(verbose_name='Ngày thử việc')
    ngaychinhthuc = models.DateField(verbose_name='Ngày làm chính thức')
    chuyenmon = models.CharField(default='', max_length=255, verbose_name='Chuyên ngành')
    vanhoa = models.CharField(default='', max_length=255, verbose_name='Trình độ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "HỒ SƠ NHÂN VIÊN"
        verbose_name_plural = 'HỒ SƠ NHÂN VIÊN'
    def __int__(self):
        return self.nhanvien


class Loaihopdong(models.Model):
    maloaihd = models.CharField(default='', max_length=255, verbose_name='Tên Hợp Đồng')
    tenhd = models.CharField(default='', max_length=255,blank=True,null=True, verbose_name='Mô Tả Hợp Đồng')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "LOẠI HỢP ĐỒNG"
        verbose_name_plural = 'LOẠI HỢP ĐỒNG'

    def __str__(self):
        return self.maloaihd

class Quanlyhopdongkinhdoanh(models.Model):
    masohopdong = models.CharField(default='',unique=True, max_length=255, verbose_name='Mã Số Hợp Đồng')
    tenhopdong  = models.CharField(default='', max_length=255, verbose_name='Tên Hợp Đồng')
    khachhang = models.CharField(default='', max_length=255, verbose_name='Tên Khách Hàng')
    ngaytrinhky = models.DateField(default='', max_length=255, verbose_name='Ngày Trình Ký Hợp Đồng')
    filehopdong = models.FileField()
    loaihd  = models.ForeignKey(Loaihopdong,default='',on_delete=models.CASCADE, verbose_name='Loại Hợp Đồng')
    nhanvien = models.ForeignKey(Nhanvien,default='',on_delete=models.CASCADE, verbose_name='Nhân Viên phụ trách')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "QUẢN LÝ HỢP ĐỒNG CÔNG TY"
        verbose_name_plural = 'QUẢN LÝ HỢP ĐỒNG CÔNG TY'

    def __int__(self):
        return self.nhanvien


class Phieuluong_upload(models.Model):
    nhanvien = models.ForeignKey(Nhanvien,on_delete=models.CASCADE)
    thang = models.CharField(default='',null=True, blank=True, max_length=255)
    nam = models.CharField(default='',null=True, blank=True, max_length=255)
    ngaylamthucte = models.CharField(default='', null=True, blank=True,max_length=255)
    congchuan = models.CharField(default='', null=True, blank=True,max_length=255)
    congthembot = models.CharField(default='',null=True, blank=True, max_length=255)
    luongcoban = models.CharField(default='',null=True, blank=True, max_length=255)
    phucap = models.CharField(default='',null=True, blank=True, max_length=255)
    tiendienthoai = models.CharField(default='', null=True, blank=True,max_length=255)
    tienxang = models.CharField(default='', null=True, blank=True,max_length=255)
    tiencom = models.CharField(default='',null=True, blank=True, max_length=255)
    luongtrachnhiem = models.CharField(default='',null=True, blank=True, max_length=255)
    tiendienthoaihotro = models.CharField(default='',null=True, blank=True, max_length=255)
    ngaynghikhongpep = models.CharField(default='',null=True, blank=True, max_length=255)
    truluongnghikhongphep = models.CharField(default='', null=True, blank=True,max_length=255)
    hotrobaohiemtrongluong = models.CharField(default='', null=True, blank=True,max_length=255)
    luoncnx2 = models.CharField(default='', null=True, blank=True,max_length=255)
    tongthunhap = models.CharField(default='', null=True, blank=True,max_length=255)
    trutienunggiuathang = models.CharField(default='',null=True, blank=True, max_length=255)
    trutienmatunggiuathang = models.CharField(default='', null=True, blank=True,max_length=255)
    trutiendienthoaicongtytraho = models.CharField(default='',null=True, blank=True, max_length=255)
    trunotrongthang = models.CharField(default='',null=True, blank=True, max_length=255)
    trubaohiem = models.CharField(default='', null=True, blank=True,max_length=255)
    trutienphat = models.CharField(default='',null=True, blank=True, max_length=255)
    truluongluyke = models.CharField(default='', null=True, blank=True,max_length=255)
    tienluongthuclanhcuoithang = models.CharField(default='',null=True, blank=True, max_length=255)
    nothangtruoc = models.CharField(default='', null=True, blank=True,max_length=255)
    muonnothangnay = models.CharField(default='', null=True, blank=True,max_length=255)
    trunotrongluong = models.CharField(default='',null=True, blank=True, max_length=255)
    thunotienmat = models.CharField(default='', null=True, blank=True, max_length=255)
    noconluanchuyensangthangsau = models.CharField(default='',null=True, blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = " UPLOAD PHIẾU LƯƠNG"
        verbose_name_plural = 'UPLOAD PHIẾU LƯƠNG'

    def __int__(self):
        return self.nhanvien


class Dexuat(models.Model):  
    
    nhanvien = models.ForeignKey(Nhanvien,on_delete=models.CASCADE)
    phongban = models.ForeignKey(Phongban,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    tieude = models.CharField(max_length=500,default="",null=False)
    noidung = RichTextUploadingField()
    files = models.FileField(blank=True,null=True,upload_to='filedexuat/')
    guiduyet= models.CharField(max_length=20, choices=[('0','Gửi Sếp'),('1',' Chỉ Gửi Trưởng Phòng')], verbose_name='Trạng Thái Gửi Duyệt')
    hangmuc = models.CharField(max_length=20, choices=[('0','Hàng Hóa'),('1','Mua Sắm Thiết Bị'),('2','Khác')], verbose_name='Hạng Mục')
    trangthaiduyet_tp = models.BooleanField()
    trangthaiduyet_sep = models.BooleanField()
    tinhtrangxem = models.BooleanField()
    tinhtranghuy = models.BooleanField()
    kinhphi = models.IntegerField(default=0)
    tinhtrangtamung = models.BooleanField()
    tientamung = models.IntegerField(default=0)
    tinhtranggiaichi = models.BooleanField(default=False)
    ghichu = models.TextField(default="",max_length=255,blank=True,null=True)
   
    thoigianhoanthanh = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:

        verbose_name = "FORM ĐỀ XUẤT"
        verbose_name_plural = 'ĐỀ XUẤT'

    def __int__(self):
        return self.nhanvien


class Giaichi(models.Model):
    dexuat = models.ForeignKey(Dexuat,on_delete=models.CASCADE,blank=True,null=True)
    nhanvien = models.ForeignKey(Nhanvien,on_delete=models.CASCADE)
    phongban = models.ForeignKey(Phongban,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    guiduyet= models.CharField(max_length=20, choices=[('0','Gửi Sếp'),('1',' Chỉ Gửi Trưởng Phòng'),('2',' Tài Chính Kế Toán')], verbose_name='Trạng Thái Gửi Duyệt')
    hangmuc = models.CharField(max_length=20, choices=[('0','Hàng Hóa'),('1','Mua Sắm Thiết Bị'),('2','Khác')], verbose_name='Hạng Mục')
    noidungdexuat =  RichTextUploadingField(null=True,blank=True)
    giaichikhac   =   RichTextUploadingField(null=True,blank=True)
    giaichihanghoa = RichTextUploadingField(blank=True,null = True,verbose_name='Hàng Hóa')
    giaichithietbi = models.JSONField(blank=True,null = True,verbose_name='Trang Thiết Bị')
    tieude = models.CharField(default="",max_length=500,null=False)
    ghichu = models.CharField(default="Thu Quy :",max_length=500,null=False)
    filegiaichi = models.FileField(null=False,blank=False,upload_to='filegiaichi/')
    trangthaiduyetgiaichi = models.BooleanField()
    trangthaiduyet_tp = models.BooleanField()
    trangthaiduyet_tckt = models.BooleanField()
    trangthaiduyet_sep = models.BooleanField()
    trangthaihuy = models.BooleanField()
    trangthaihoanthanh = models.BooleanField()
    noidungthanhtoan =  RichTextUploadingField(null=True,blank=True)
    tientamung  = models.IntegerField(default=0)
    tiengiaichi = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:

        verbose_name = "GIAI CHI "
        verbose_name_plural = 'GIAI CHI'

    def __int__(self):
        return self.nhanvien

class Phanquyen(models.Model):
    nhanvien = models.ForeignKey(Nhanvien,on_delete=models.CASCADE)
    phongban = models.ForeignKey(Phongban,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE ,blank=True,null=True)
    quyenxem = models.BooleanField()
    quyensua = models.BooleanField()
    quyendsp = models.BooleanField()
    quyenxemketoan = models.BooleanField()
    quyensuaketoan = models.BooleanField()
    quyenxemhcns =models.BooleanField()
    quyensuahcns = models.BooleanField()
    quyenxemkho =models.BooleanField()
    quyensuakho = models.BooleanField()
    quyenxempbs = models.BooleanField()
    quyensuapbs = models.BooleanField()

    class Meta:

        verbose_name = "PHÂN QUYỀN"
        verbose_name_plural = "PHÂN QUYỀN"

    def __int__(self):
        return self.nhanvien
    
    
