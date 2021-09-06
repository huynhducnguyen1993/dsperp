from qlns.models import Nhanvien
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.db import models
from django.contrib import admin
from django.db.models.fields.related import OneToOneField
from django.utils.html import format_html
from django.contrib.auth.models import AbstractUser,User
from ckeditor.fields import *
from ckeditor_uploader.fields import *
from qlns.models import *
# Create your models here.

class Tkhd(models.Model):
    
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    nhanvien = models.ForeignKey(Nhanvien,on_delete=models.CASCADE)
    phongban = models.ForeignKey(Phongban,on_delete=models.CASCADE)
    mahopdong =models.CharField(default="", max_length=50 ,blank=True,null=True)
    tieude = models.CharField(default="",max_length=255 )
    khachhang = models.CharField(default='',max_length=255 )
    
    file = models.FileField(upload_to="filetkhd/")
    ghichu = models.CharField(default="",max_length=1000,null=True,blank=True)
    guiduyet= models.CharField(max_length=20, choices=[('0','Gửi Anh Thắng'),('1',' Chỉ Gửi Trưởng Phòng')], verbose_name='Trạng Thái Gửi Duyệt')
    trangthaiduyet_tp = models.BooleanField(default=False)
    trangthaiduyet_at = models.BooleanField(default=False)
    trinhtrangduyet_huy = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.tieude



