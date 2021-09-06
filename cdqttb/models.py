from django.contrib.auth import *
from django.db import models
from django.contrib import admin
from django.db.models.fields.related import OneToOneField
from django.utils.html import format_html
from django.contrib.auth.models import AbstractUser,User
from ckeditor.fields import *
from ckeditor_uploader.fields import *
from qlns.models import *



class Danhmucthongbao(models.Model):
    tendanhmuc = models.CharField(max_length=255,default='',verbose_name="Tên Danh Mục ")
    mota = models.CharField(max_length=1000,default="",verbose_name="Mô tả danh mục")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Danh Mục Thông Báo"
        verbose_name_plural = 'Danh Mục Thông Báo'



    def __str__(self):
        return self.tendanhmuc

class Thongbao(models.Model):
    tieude = models.CharField(default='',max_length=255,verbose_name='Tiêu đề thông báo')
    danhmuc = models.ForeignKey(Danhmucthongbao,on_delete=models.CASCADE,verbose_name="Chọn Danh Mục")
    noidung = RichTextUploadingField(verbose_name='Nội Dung Thông Báo')
    tacgia = models.ForeignKey(Nhanvien,on_delete=models.CASCADE,verbose_name='Tác Giả')
    phongban = models.ForeignKey(Phongban,default='',null=True,blank=True,on_delete=models.CASCADE,verbose_name="Phòng ban Áp dụng -Nêu Công Ty thì không chọn ")
    hienthi = models.BooleanField(verbose_name='Check : Cho hiển thị  - Uncheck : Tắt hiển thị')
    huy = models.BooleanField(verbose_name='Hủy Thông báo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Thông Báo"
        verbose_name_plural = 'Thông Báo'


    def __str__(self):
        return self.tieude

class Thongbao(models.Model):
    tieude = models.CharField(default='',max_length=255,verbose_name='Tiêu đề thông báo')
    danhmuc = models.ForeignKey(Danhmucthongbao,on_delete=models.CASCADE,verbose_name="Chọn Danh Mục")
    noidung = RichTextUploadingField(verbose_name='Nội Dung Thông Báo')
    tacgia = models.ForeignKey(Nhanvien,on_delete=models.CASCADE,verbose_name='Tác Giả')
    phongban = models.ForeignKey(Phongban,default='',null=True,blank=True,on_delete=models.CASCADE,verbose_name="Phòng ban Áp dụng -Nêu Công Ty thì không chọn ")
    hienthi = models.BooleanField(verbose_name='Check : Cho hiển thị  - Uncheck : Tắt hiển thị')
    huy = models.BooleanField(verbose_name='Hủy Thông báo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Thông Báo"
        verbose_name_plural = 'Thông Báo'


    def __str__(self):
        return self.tieude
        


class Quytrinh(models.Model):
    tenquytrinh = models.CharField(default='',max_length=255,verbose_name='Tên quy trình')
    noidung = RichTextUploadingField(verbose_name='Nội Dung quy trình')
    tacgia = models.ForeignKey(Nhanvien,on_delete=models.CASCADE,verbose_name='Tác Giả')
    hienthi = models.BooleanField(verbose_name='Check : Cho hiển thị  - Uncheck : Tắt hiển thị')
    huy = models.BooleanField(verbose_name='Hủy Thông báo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Quy Trình Công Ty"
        verbose_name_plural = 'Quy Trình Công Ty'
    
    def __str__(self):
        return self.tenquytrinh


class Quytrinhphongban(models.Model):
    tenquytrinh = models.CharField(default='',max_length=255,verbose_name='Tên quy trình')
    noidung = RichTextUploadingField(verbose_name='Nội Dung quy trình')
    phongban = models.ForeignKey(Phongban,on_delete=models.CASCADE,verbose_name="Phòng ban áp dụng")
    tacgia = models.ForeignKey(Nhanvien,on_delete=models.CASCADE,verbose_name='Tác Giả')
    hienthi = models.BooleanField(verbose_name='Check : Cho hiển thị  - Uncheck : Tắt hiển thị')
    huy = models.BooleanField(verbose_name='Hủy Thông báo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Quy Trình Phòng Ban"
        verbose_name_plural = 'Quy Trình Phòng Ban'
    
    def __str__(self):
        return self.tenquytrinh 


class Quytrinhcongty(models.Model):
    tenquytrinh = models.CharField(default='',max_length=255,verbose_name='Tên quy trình')
    noidung = RichTextUploadingField(verbose_name='Nội Dung quy trình')
    tacgia = models.ForeignKey(Nhanvien,on_delete=models.CASCADE,verbose_name='Tác Giả')
    hienthi = models.BooleanField(verbose_name='Check : Cho hiển thị  - Uncheck : Tắt hiển thị')
    huy = models.BooleanField(verbose_name='Hủy quy trình')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Quy Trình Công Ty"
        verbose_name_plural = 'Quy Trình Công Ty'
    
    def __str__(self):
        return self.tenquytrinh   


class Quydinhphongban(models.Model):
    tenquydinh = models.CharField(default='',max_length=255,verbose_name='Tên quy định')
    noidung = RichTextUploadingField(verbose_name='Nội Dung quy định')
    phongban = models.ForeignKey(Phongban,on_delete=models.CASCADE,verbose_name="Phòng ban áp dụng")
    tacgia = models.ForeignKey(Nhanvien,on_delete=models.CASCADE,verbose_name='Tác Giả')
    hienthi = models.BooleanField(verbose_name='Check : Cho hiển thị  - Uncheck : Tắt hiển thị')
    huy = models.BooleanField(verbose_name='Hủy quy định')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Quy Định Phòng Ban"
        verbose_name_plural = 'Quy Định Phòng Ban'
    
    def __str__(self):
        return self.tenquydinh


class Quydinhcongty(models.Model):
    tenquydinh = models.CharField(default='',max_length=255,verbose_name='Tên quy định')
    noidung = RichTextUploadingField(verbose_name='Nội Dung quy định')
    tacgia = models.ForeignKey(Nhanvien,on_delete=models.CASCADE,verbose_name='Tác Giả')
    hienthi = models.BooleanField(verbose_name='Check : Cho hiển thị  - Uncheck : Tắt hiển thị')
    huy = models.BooleanField(verbose_name='Hủy quy định')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Quy Định Công Ty"
        verbose_name_plural = 'Quy Định Công Ty'
    
    def __str__(self):
        return self.tenquydinh




class Chedophongban(models.Model):
    tenchedo = models.CharField(default='',max_length=255,verbose_name='Tên Chế Độ')
    noidung = RichTextUploadingField(verbose_name='Nội Dung Chế Độ ')
    phongban = models.ForeignKey(Phongban,on_delete=models.CASCADE,verbose_name="Phòng ban áp dụng")
    tacgia = models.ForeignKey(Nhanvien,on_delete=models.CASCADE,verbose_name='Tác Giả')
    hienthi = models.BooleanField(verbose_name='Check : Cho hiển thị  - Uncheck : Tắt hiển thị')
    huy = models.BooleanField(verbose_name='Hủy Chế Độ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Chế Độ Phòng Ban"
        verbose_name_plural = 'Chế Độ Phòng Ban'
    
    def __str__(self):
        return self.tenchedo   


class Chedocongty(models.Model):
    tenchedo = models.CharField(default='',max_length=255,verbose_name='Tên Chế Độ')
    noidung = RichTextUploadingField(verbose_name='Nội Dung Chế Độ ')
    tacgia = models.ForeignKey(Nhanvien,on_delete=models.CASCADE,verbose_name='Tác Giả')
    hienthi = models.BooleanField(verbose_name='Check : Cho hiển thị  - Uncheck : Tắt hiển thị')
    huy = models.BooleanField(verbose_name='Hủy Chế Độ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Chế Độ Công Ty"
        verbose_name_plural = 'Chế Độ Công Ty'
    
    def __str__(self):
        return self.tenchedo   





