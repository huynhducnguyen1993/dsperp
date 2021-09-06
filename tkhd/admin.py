from django.contrib import admin
from .models import *
# Register your models here.

class Tkhdadmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        get_data = super(Tkhdadmin, self).get_changeform_initial_data(request)
        get_data['username'] = request.user.pk
        nhanvien = Nhanvien.objects.get(username = request.user)
        get_data['nhanvien'] = nhanvien
        get_data['phongban'] = nhanvien.phongban
        return get_data

admin.site.register(Tkhd, Tkhdadmin)