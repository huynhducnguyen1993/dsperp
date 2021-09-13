from athuvien.models import Catalog
from django.contrib import admin
from .forms import *
from qlns.models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ExportActionMixin
from datetime import datetime
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
# Register your models here.


class DanhmucAdmins(admin.ModelAdmin):
    list_display = ('id','tendanhmuc', 'created_at')
    search_fields = ('tencatalog',)
    list_filter = ('created_at',)
    list_per_page = 20
    
    skip_unchanged = True
    report_skipped = True
    
    exclude = ('id',)
   
admin.site.register(DanhmucCatalog,DanhmucAdmins)

class Hangdmins(admin.ModelAdmin):
    list_display = ('id','tenhang', 'created_at')
    search_fields = ('tenhang',)
    list_filter = ('created_at',)
    list_per_page = 20
    
    skip_unchanged = True
    report_skipped = True
    
    exclude = ('id',)
   
admin.site.register(HangCatalog,Hangdmins)


class CatalogAdmins(admin.ModelAdmin):
    list_display = ('id','danhmuccatalog', 'hangcatalog' ,'tencatalog','created_at')
    search_fields = ('tencatalog',)
    list_filter = ('danhmuccatalog',)
    list_per_page = 20
    import_id_fields = ('code',)
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)
    form = CatalogForm 

        
admin.site.register(Catalog,CatalogAdmins)