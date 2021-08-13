from django.db import models
from django.contrib.auth import *
from django.contrib import admin
from django.db.models.fields import BooleanField
from qlns.models import *
from django.db.models.fields.related import OneToOneField
from django.utils.html import format_html
from django.contrib.auth.models import AbstractUser,User
from ckeditor.fields import *
from ckeditor_uploader.fields import *

# Create your models here.

class Khachhanglon(models.Model):
    nhanvien = models.ForeignKey(Nhanvien,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    phongban = models.ForeignKey(Phongban,on_delete=models.CASCADE)
    tenkhachhang = models.CharField(max_length=255,default="",verbose_name="Tên Khách Hàng")
    diachikh = models.CharField(null =True,blank=True,default="",max_length=255,verbose_name="Địa Chỉ Khách Hàng")
    tencongtrinh = models.CharField(null =True,blank=True,default="",max_length=255,verbose_name="Tên Công Trình")
    diachicongtrinh =models.CharField(null =True,blank=True,default="",max_length=255,verbose_name="Địa Chỉ Công Trình")
    hangmuc =  models.CharField(max_length=20, choices=[('0','Hàng Hóa'),('1',' Lắp Đặt'),('2',' Phân phối Lắp Đặt'),('3','Dịch Vụ')], verbose_name='Hạng Mục Hợp Đồng')
    noidung = RichTextUploadingField(null=True,blank=True,default="")
    baogia = models.BooleanField(default=False,blank=True,null=True,verbose_name="Báo Giá")
    thuongthaohopdong = models.BooleanField(default=False,blank=True,null=True,verbose_name="Thương Thảo Hợp Đồng")
    kyhopdong = models.BooleanField(default=False,blank=True,null=True,verbose_name="Ký Hợp Đồng")
    huytheo =  models.BooleanField(default=False,blank=True,null=True,verbose_name="Hủy Theo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:

        verbose_name = "KHÁCH HÀNG LỚN"
        verbose_name_plural = 'KHÁCH HÀNG LỚN'

    def __int__(self):
        return self.nhanvien