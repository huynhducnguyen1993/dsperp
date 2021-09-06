"""erp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.static import serve 
from django.urls import path,include
from qlns.views import *
from khovan.views import *
from cdqttb.views import *
from khachhang.views import *
from django.conf import settings
from django.conf.urls import url 
from django.conf.urls.static import static

admin.site.index_title="Quản Trị Hệ Thống"
urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),
    path('pdf/', include('mergepdf.urls')),
    path('tasks/', include('tasks.urls')),
    path('trinh-ky-hop-dong/', include('tkhd.urls',namespace='trinh-ky')),
    
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('', Index.as_view(),name='index'),
    path('login/', Login.as_view(),name='login'),
    path('logout',Logout.as_view(),name='logout'),
    path('api-auth/', include('rest_framework.urls')),
    path('nhan-vien/zoom/' ,Zoom.as_view(),name='zoom' ),

    path('load-bang-cong/', Loadbangcong.as_view(),name='load-bang-cong'),
   
    
    
    path('get-nhan-vien/', Getnhanvien.as_view(),name='getnhanvien'),
    path('profile/',Profile.as_view(),name='profile'),
    path('dsnhanvien/',Dsnhanvien.as_view(),name='dsnhanvien'),
    path('viewnhanvien/', Viewnhanvien.as_view(), name='viewnhanvien'),
    path('deletenhanvien/',Delete_checkbox.as_view(), name='delete-nhanvien'),
    path('phieu-luong-upload/',Phieuluongupload.as_view(), name='phieuluongupload'),
    path('nhanvien/delete/ed5511ad61be3b785518eddc96e4bc3f<int:nhanvien_id>',Deletenhanvien.as_view(),name='deletenhanvien'),
    path('nhan-vien/xem-nhan-vien/ed5511ad61be3b785518eddc96e4bc3f<int:nhanvien_id>', Changenhanvien.as_view(), name='xemnhanvien'),
    path('phieu-luong/nhan-vien/<int:nhanvien_id>ed5511ad61be3b785518eddc96e4bc3f', Phieuluongcanhan.as_view(), name='xemphieuluong'),
    path('phieu-luong-user', Phieuluonguser.as_view(), name='xemphieuluonguser'),

    path('nhan-vien/tao-de-xuat.chelsea',Dexuats.as_view(),name='form-de-xuat'),
    path('nhan-vien/de-xuat-chua-duyet/',Dexuatchuaduyet.as_view(),name='dexuat-chua-duyet'),
    path('nhan-vien/de-xuat-da-duyet/',Dexuatdaduyet.as_view(),name='dexuat-da-duyet'),
    path('nhan-vien/de-xuat-khong-phe-duyet/',Dexuathuy.as_view(),name='dexuat-huy'),
    path('nhan-vien/quan-ly-de-xuat/chua-duyet/',Quanlydexuat.as_view(),name='quan-ly-de-xuat'),
    path('nhan-vien/quan-ly-de-xuat/sep-chua-duyet/',Quanlydexuat_sepduyet.as_view(),name='quan-ly-de-xuat-sep'),
    path('nhan-vien/de-xuat/ed5511ad61be3b785518eddc96e4bc3f<int:dexuat_id>', Xulyduyet_tp.as_view(), name='xu-ly-duyet-tp'),
    path('nhan-vien/de-xuat/duyet-de-xuat/ed5511ad61be3b785518eddc96e4bc3f<int:dexuat_id>', Xulyduyet_sep.as_view(), name='xu-ly-duyet-sep'),
    path('nhan-vien/quan-ly-de-xuat/da-duyet/',Quanlydexuat_daduyet.as_view(),name='quan-ly-de-xuat-da-duyet'),
    path('nhan-vien/quan-ly-de-xuat/da-tam-ung/',Quanlydexuat_datamung.as_view(),name='quan-ly-de-xuat-da-tam-ung'),
    path('nhan-vien/quan-ly-de-xuat/da-giai-chi/',Quanlydexuat_dagiaichi.as_view(),name='quan-ly-de-xuat-da-giai-chi'),
    path('nhan-vien/quan-ly-de-xuat/da-huy/',Quanlydexuat_dahuy.as_view(),name='quan-ly-de-xuat-da-huy'),
    path('nhan-vien/de-xuat/xem-de-xuat/ed5511ad61be3b785518eddc96e4bc3f<int:dexuat_id>ed5511ad61be3b785518eddc96e4bc3f',View_dexuat.as_view(),name='view-dexuat'),
    path('nhan-vien/de-xuat/xem-de-xuat-lq/25a2af956c975b7025a67804f2abc47b-<int:dexuat_id>-25a2af956c975b7025a67804f2abc47b/57b40ec81c10f53c2e5f2c15aa456714/<int:hash_id>/57b40ec81c10f53c2e5f2c15aa456714',View_dexuat_lq.as_view(),name='view-dexuat-lq'),
    path('nhan-vien/de-xuat/sua-de-xuat/ed5511ad61be3b785518eddc96e4bc3f<int:dexuat_id>ed5511ad61be3b785518eddc96e4bc3f',Editdexuat.as_view(),name='edit-dexuat'),

    path('nhan-vien/quan-ly-giai-chi/nhap-tam-ung/',Nhaptamung.as_view(),name='nhap-tam-ung'),
    path('nhan-vien/quan-ly-giai-chi/da-tam-ung/',Datamung.as_view(),name='da-tam-ung'),
    path('nhan-vien/quan-ly-giai-chi/form-da-tam-ung/ed5511ad61be3b785518eddc96e4bc3f<int:dexuat_id>',Formnhap_tamung.as_view(),name='form-nhap-tam-ung'),
    path('nhan-vien/quan-ly-giai-chi/form-dieu-chinh-tam-ung/<int:dexuat_id>',Formdieuchinh_tamung.as_view(),name='form-dieu-chinh-tam-ung'),
    path('nhan-vien/giai-chi/tao-giai-chi/',Taogiaichi.as_view(),name='tao-giai-chi'),
    path('nhan-vien/giai-chi/tao-giai-chi-tu-de-xuat/ed5511ad61be3b785518eddc96e4bc3f<int:dexuat_id>',Giaichi_dx.as_view(),name='tao-giai-chi-dx'),
    path('nhan-vien/quan-ly-giai-chi/tao-giai-chi-hang-hoa-moi/',Giaichihanghoa_moi.as_view(),name='tao-giai-chi-hang-hoa-moi'),
    path('nhan-vien/quan-ly-giai-chi/tao-giai-chi-khac-moi/',Giaichikhac_moi.as_view(),name='tao-giai-chi-khac-moi'),
    path('nhan-vien/quan-ly-giai-chi/tao-giai-chi-thiet-bi-moi/',Giaichithietbi_moi.as_view(),name='tao-giai-chi-thiet-bi-moi'),
    path('nhan-vien/quan-ly-giai-chi/giai-chi-chua-duyet/',Giaichichuaduyet.as_view(),name='giai-chi-chua-duyet'),
    path('nhan-vien/quan-ly-giai-chi/giai-chi-da-duyet/',Giaichidaduyet.as_view(),name='giai-chi-da-duyet'),
    path('nhan-vien/quan-ly-giai-chi/giai-chi-da-huy/',Giaichidahuy.as_view(),name='giai-chi-da-huy'),
    path('nhan-vien/quan-ly-giai-chi/giai-chi-da-thanh-toan/',Giaichidathanhtoan.as_view(),name='giai-chi-da-thanh-toan'),
    path('nhan-vien/giai-chi/view-giai-chi/ed5511ad61be3b785518eddc96e4bc3f<int:giaichi_id>',View_giaichi.as_view(),name='view-giai-chi'),
    path('nhan-vien/giai-chi/edit-giai-chi/ed5511ad61be3b785518eddc96e4bc3f<int:giaichi_id>',Edit_giaichi.as_view(),name='edit-giai-chi'),
    path('nhan-vien/giai-chi/view-giai-chi-tp/ed5511ad61be3b785518eddc96e4bc3f<int:giaichi_id>',View_giaichi_tp.as_view(),name='view-giai-chi-tp'),
    path('nhan-vien/giai-chi/bao-cao-giai-chi/',Baocaogiaichi.as_view(),name='bao-cao-giai-chi'),
    path('load-gia-chi/', Loadgiaichi.as_view(), name='load-giai-chi'),

 
    path('nhan-vien/quan-ly-giai-chi/',Quanlygiaichi.as_view(),name='quan-ly-giai-chi-tp'),
    path('nhan-vien/quan-ly-giai-chi-tckt/',Quanlygiaichi_tckt.as_view(),name='quan-ly-giai-chi-tckt'),
    path('nhan-vien/quan-ly-giai-chi-tckt/ed5511ad61be3b785518eddc96e4bc3f<int:giaichi_id>ed5511ad61be3b785518eddc96e4bc3f',Xu_ly_giai_chi_tckt.as_view(),name='xu-ly-giai-chi-tckt'),
    path('nhan-vien/quan-ly-giai-chi-sep/',Quanlygiaichi_sep.as_view(),name='quan-ly-giai-chi-sep'),
    path('nhan-vien/quan-ly-giai-chi/ql-giai-chi-da-duyet',Quanlygiaichi_daduyet.as_view(),name='quan-ly-giaichi-da-duyet'),
    path('nhan-vien/quan-ly-giai-chi/ql-giai-chi-da-hoan-thanh',Quanlygiaichi_hoanthanh.as_view(),name='quan-ly-giaichi-da-hoan-thanh'),
    path('nhan-vien/quan-ly-giai-chi/ql-giai-chi-da-huy',Quanlygiaichi_dahuy.as_view(),name='quan-ly-giaichi-da-huy'),
    path('nhan-vien/quan-ly-giai-chi/xu-ly-giai-chi-tp/ed5511ad61be3b785518eddc96e4bc3f<int:giaichi_id>ed5511ad61be3b785518eddc96e4bc3f',Xu_ly_giai_chi.as_view(),name='xu-ly-giai-chi-tp'),
    path('nhan-vien/quan-ly-giai-chi/xu-ly-giai-chi-sep/ed5511ad61be3b785518eddc96e4bc3f<int:giaichi_id>ed5511ad61be3b785518eddc96e4bc3f',Xu_ly_giai_chi.as_view(),name='xu-ly-giai-chi-sep'),

    path('nhan-vien/nhap-khach-hang-lon/',Create_khl.as_view(),name="nhap-khach-hang-lon"),
    path('nhan-vien/danh-sach-khach-hang-lon/',Danhsach_khachhanglon.as_view(),name="danh-sach-khach-hang-lon"),
    path('nhan-vien/xem-sach-khach-hang-lon/ed5511ad61be3b785518eddc96e4bc3f<int:khachhang_id>',View_khachhanglon.as_view(),name="xem-khach-hang-lon"),
    path('nhan-vien/sua-sach-khach-hang-lon/<int:khachhang_id>ed5511ad61be3b785518eddc96e4bc3f',Edit_khachhanglon.as_view(),name="sua-khach-hang-lon"),

    path('nhan-vien/thu-quy/thanh-toan-giai-chi/',Thanhtoan_giaichi.as_view(),name="thanh-toan-giai-chi"),
    path('nhan-vien/thu-quy/thanh-toan-giai-chi/ed5511ad61be3b785518eddc96e4bc3fed5511ad61be3b785518eddc96e4bc3fed5511ad61be3b785518eddc96e4bc3f<int:giaichi_id>ed5511ad61be3b785518eddc96e4bc3f',Xacnhanthanhtoan_giaichi.as_view(),name="nhap-thanh-toan-giai-chi"),

    path('nhap-hang/',Nhaphangs.as_view(),name="nhap-hang"),
    path('sua-phieu-nhap-hang/ed5511ad61be3b785518eddc96e4bc3f<int:code_id>ed5511ad61be3b785518eddc96e4bc3f',Viewphieunhap.as_view(),name='view-nhap-hang'),
    path('phieu-nhap-kho/',Phieunhapkho.as_view(),name="phieu-nhap-kho"),
    path('load-courses/', load_courses.as_view(), name='ajax_load_courses'),
    path('quan-ly-nhap-hang',Quanlynhaphang.as_view(),name="quan-ly-nhap-hang"),
    path('nhap-hang-chua-duyet',Nhaphangchuaduyet.as_view(),name='nhaphangchuaduyet'),
    path('nhap-hang-chua-duyet-gap',Nhaphangchuaduyetgap.as_view(),name='nhaphangchuaduyetgap'),
    path('duyet-nhap-hang/<int:code_id>',Duyetnhaphang.as_view(),name='duyetnhaphang'),
    path('phieu-nhap-hang/da-duyet/',Nhaphangdaduyet.as_view(),name='nhaphangdapheduyet'),
    path('xuat-hang/',Xuathang.as_view(),name="xuat-hang"),
    path('ton-kho/',Tonkho.as_view(),name="ton-kho"),
    path('kho-van/thu-kho-can-xu-ly/',Thukho_Canxuly.as_view(),name="thu-kho-can-xu-ly"),
    path('kho-van/thu-kho-can-xu-ly/<int:code_id>',Formxulynhapkho.as_view(),name="form-thu-kho-can-xu-ly"),
    path('kho-van/thu-kho-treo/',Thukho_Treo.as_view(),name="thu-kho-treo"),
    path('dieu-chuyen-kho/',Dieuchuyenkho.as_view(),name="dieu-chuyen-kho"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}), 
              ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
