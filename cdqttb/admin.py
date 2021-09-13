from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ExportActionMixin
from qlns.models import *
from cdqttb.resources import ThongbaoResource
from datetime import datetime
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from django import forms
from cdqttb.forms import *
# Register your models here.



admin.site.site_header="Đông Sapa"



class ThongbaoAdmins(ImportExportActionModelAdmin):
    list_display = ('id','danhmuc', 'tieude' ,'created_at')
    search_fields = ('tieude',)
    list_filter = ('danhmuc',)
    list_per_page = 20
    import_id_fields = ('code',)
    skip_unchanged = True
    report_skipped = True
    resource_class =ThongbaoResource
    exclude = ('id',)
    form = ThongbaoForm

    def get_form(self, request, obj=None, **kwargs):
        nhanvien = Nhanvien.objects.filter(username = request.user)
        form = super(ThongbaoAdmins, self).get_form(request, obj=None, **kwargs)
        form.base_fields['tacgia'].queryset = nhanvien
        
        
        return form

    

admin.site.register(Thongbao, ThongbaoAdmins)


# class DanhmucAdmin(ImportExportActionModelAdmin):
#     list_display = ('id','tendanhmuc','view_baiviet')
#     import_id_fields = ('code',)
#     skip_unchanged = True
#     report_skipped = True
#     def view_baiviet(self,obj):
#         count = obj.thongbao_set.count()
#         url = (
#                 reverse("admin:cdqttb_thongbao_changelist")
#                 + "?"
#                 + urlencode({"danhmuc__id": f"{obj.id}"})
#         )
#         return format_html('<a href="{}">{} Bài Viết</a>', url, count)

#     view_baiviet.short_description = "Số Thông Báo"
#     # tính tổng nhân viên trong 1 phòngs

#     def before_save_instance(self, instance):
#         format_str = '%d/%m/%y'  # the format in which dates are stored in CSV file
#         instance.created_at = datetime.strptime(instance.created_at, format_str)
#         instance.updated_at = datetime.strptime(instance.updated_at, format_str)
#         return instance



# admin.site.register(Danhmucthongbao, DanhmucAdmin)



class QuytrinhphongbanAdmins(ImportExportActionModelAdmin):
    list_display = ('id', 'tenquytrinh' ,'created_at')
    search_fields = ('tenquytrinh',)
    list_filter = ('created_at',)
    list_per_page = 20
    import_id_fields = ('code',)
    skip_unchanged = True
    report_skipped = True
   
    exclude = ('id',)
    form = QuyTrinhphongbanForm

    def get_form(self, request, obj=None, **kwargs):
        nhanvien = Nhanvien.objects.filter(username = request.user)
        form = super(QuytrinhphongbanAdmins, self).get_form(request, obj=None, **kwargs)
        form.base_fields['tacgia'].queryset = nhanvien
        
        
        return form


admin.site.register(Quytrinhphongban, QuytrinhphongbanAdmins)


class QuytrinhcongtyAdmins(ImportExportActionModelAdmin):
    list_display = ('id', 'tenquytrinh' ,'created_at')
    search_fields = ('tenquytrinh',)
    list_filter = ('created_at',)
    list_per_page = 20
    import_id_fields = ('code',)
    skip_unchanged = True
    report_skipped = True
   
    exclude = ('id',)
    form = QuyTrinhcongtyForm

    def get_form(self, request, obj=None, **kwargs):
        nhanvien = Nhanvien.objects.filter(username = request.user)
        form = super(QuytrinhcongtyAdmins, self).get_form(request, obj=None, **kwargs)
        form.base_fields['tacgia'].queryset = nhanvien
        
        
        return form


admin.site.register(Quytrinhcongty, QuytrinhcongtyAdmins)


class QuydinhphongbanAdmins(ImportExportActionModelAdmin):
    list_display = ('id', 'tenquydinh','phongban' ,'created_at')
    search_fields = ('tenquydinh',)
    list_filter = ('created_at',)
    list_per_page = 20
    import_id_fields = ('code',)
    skip_unchanged = True
    report_skipped = True
   
    exclude = ('id',)
    form = QuyDinhphongbanForm

    def get_form(self, request, obj=None, **kwargs):
        nhanvien = Nhanvien.objects.filter(username = request.user)
        form = super(QuydinhphongbanAdmins, self).get_form(request, obj=None, **kwargs)
        form.base_fields['tacgia'].queryset = nhanvien
        
        
        return form



admin.site.register(Quydinhphongban, QuydinhphongbanAdmins)


class QuydinhcongtyAdmins(ImportExportActionModelAdmin):
    list_display = ('id', 'tenquydinh' ,'created_at')
    search_fields = ('tenquydinh',)
    list_filter = ('created_at',)
    list_per_page = 20
    import_id_fields = ('code',)
    skip_unchanged = True
    report_skipped = True
   
    exclude = ('id',)
    form = QuyDinhcongtyForm

    def get_form(self, request, obj=None, **kwargs):
        nhanvien = Nhanvien.objects.filter(username = request.user)
        form = super(QuydinhcongtyAdmins, self).get_form(request, obj=None, **kwargs)
        form.base_fields['tacgia'].queryset = nhanvien
        
        
        return form



admin.site.register(Quydinhcongty, QuydinhcongtyAdmins)



class ChedocongtyAdmins(ImportExportActionModelAdmin):
    list_display = ('id', 'tenchedo' ,'created_at')
    search_fields = ('tenchedo',)
    list_filter = ('created_at',)
    list_per_page = 20
    import_id_fields = ('code',)
    skip_unchanged = True
    report_skipped = True
   
    exclude = ('id',)
    form = QuyDinhcongtyForm

    def get_form(self, request, obj=None, **kwargs):
        nhanvien = Nhanvien.objects.filter(username = request.user)
        form = super(ChedocongtyAdmins, self).get_form(request, obj=None, **kwargs)
        form.base_fields['tacgia'].queryset = nhanvien
        
        
        return form



admin.site.register(Chedocongty, ChedocongtyAdmins)


class ChedophongbanAdmins(ImportExportActionModelAdmin):
    list_display = ('id', 'tenchedo' ,'created_at')
    search_fields = ('tenchedo',)
    list_filter = ('created_at',)
    list_per_page = 20
    import_id_fields = ('code',)
    skip_unchanged = True
    report_skipped = True
   
    exclude = ('id',)
    form = QuyDinhcongtyForm

    def get_form(self, request, obj=None, **kwargs):
        nhanvien = Nhanvien.objects.filter(username = request.user)
        form = super(ChedophongbanAdmins, self).get_form(request, obj=None, **kwargs)
        form.base_fields['tacgia'].queryset = nhanvien
        
        
        return form



admin.site.register(Chedophongban, ChedophongbanAdmins)



