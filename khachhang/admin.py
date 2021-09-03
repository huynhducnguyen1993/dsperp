from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ExportActionMixin
from qlns.models import Nhanvien
from qlns.resources import NhanvienResource
from datetime import datetime
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

# Register your models here.


class KhachhanglonAdmins(ImportExportActionModelAdmin):
    list_display = ('id','nhanvien','phongban', 'hangmuc', 'tencongtrinh', 'diachicongtrinh',)
    search_fields = ('tencongtrinh',) 
    list_filter = ('phongban',)
    list_per_page = 10
    import_id_fields = ('id',)
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)
    
admin.site.register(Khachhanglon,KhachhanglonAdmins)
