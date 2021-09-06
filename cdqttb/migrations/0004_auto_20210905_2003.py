# Generated by Django 3.2.7 on 2021-09-05 13:03

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qlns', '0028_alter_dexuat_nhanviencc'),
        ('cdqttb', '0003_danhmucthongbao_quydinhcongty_quydinhphongban_quytrinh_quytrinhcongty_quytrinhphongban_thongbao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quydinhcongty',
            name='huy',
            field=models.BooleanField(verbose_name='Hủy quy định'),
        ),
        migrations.AlterField(
            model_name='quydinhcongty',
            name='noidung',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Nội Dung quy định'),
        ),
        migrations.CreateModel(
            name='Chedophongban',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenchedo', models.CharField(default='', max_length=255, verbose_name='Tên Chế Độ')),
                ('noidung', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Nội Dung Chế Độ ')),
                ('hienthi', models.BooleanField(verbose_name='Check : Cho hiển thị  - Uncheck : Tắt hiển thị')),
                ('huy', models.BooleanField(verbose_name='Hủy Chế Độ')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phongban', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qlns.phongban', verbose_name='Phòng ban áp dụng')),
                ('tacgia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qlns.nhanvien', verbose_name='Tác Giả')),
            ],
            options={
                'verbose_name': 'Chế Độ Phòng Ban',
                'verbose_name_plural': 'Chế Độ Phòng Ban',
            },
        ),
        migrations.CreateModel(
            name='Chedocongty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenchedo', models.CharField(default='', max_length=255, verbose_name='Tên Chế Độ')),
                ('noidung', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Nội Dung Chế Độ ')),
                ('hienthi', models.BooleanField(verbose_name='Check : Cho hiển thị  - Uncheck : Tắt hiển thị')),
                ('huy', models.BooleanField(verbose_name='Hủy Chế Độ')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tacgia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qlns.nhanvien', verbose_name='Tác Giả')),
            ],
            options={
                'verbose_name': 'Chế Độ Công Ty',
                'verbose_name_plural': 'Chế Độ Công Ty',
            },
        ),
    ]
