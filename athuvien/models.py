from django.contrib.auth import *
from django.db import models
from django.contrib import admin
from django.db.models.fields.related import OneToOneField
from django.utils.html import format_html
from django.contrib.auth.models import AbstractUser,User
from ckeditor.fields import *
from ckeditor_uploader.fields import *
from qlns.models import *
from cdqttb.models import *


# Create your models here.
class DanhmucCatalog(models.Model):
    tendanhmuc = models.CharField(default="" ,max_length=255,verbose_name="Tên Danh Mục Catalog ")
    motadanhmuc = models.CharField(default="",blank=True,null=True,max_length=255, verbose_name='Mô Tẩ Danh Mục ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Danh Mục Catalog "
        verbose_name_plural = 'Danh Mục Catalog '


    def __str__(self):
        return self.tendanhmuc

class HangCatalog(models.Model):
    tenhang = models.CharField(default="" ,max_length=255,verbose_name="Tên Danh Mục Catalog ")
    motahang = models.CharField(default="",blank=True,null=True,max_length=255, verbose_name='Mô Tẩ Danh Mục ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Hãng Catalog "
        verbose_name_plural = 'Hãng Catalog '


    def __str__(self):
        return self.tenhang

class Catalog(models.Model):
    tencatalog = models.CharField(default="",max_length=255,verbose_name="Tên Catalog ")
    motacatalog = models.CharField(default="",max_length=255,blank=True,null=True,verbose_name="Mô Tả Catalog (Có Thể bỏ Trống)")
    danhmuccatalog = models.ForeignKey(DanhmucCatalog,on_delete=models.CASCADE,verbose_name='Chọn Danh Mục')
    hangcatalog = models.ForeignKey(HangCatalog,on_delete=models.CASCADE,verbose_name='Chọn Hãng ')
    filecatalog = models.FileField(default="",upload_to="thuvien/file_catalog/")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Bài viết Catalog "
        verbose_name_plural = 'Bài viết Catalog  '


    def __str__(self):
        return self.tencatalog