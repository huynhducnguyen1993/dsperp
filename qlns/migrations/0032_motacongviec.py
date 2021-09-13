# Generated by Django 3.2.7 on 2021-09-06 07:13

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qlns', '0031_alter_nhanvien_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motacongviec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieude', models.CharField(default='', max_length=255, verbose_name='Tiêu Đề Công Việc')),
                ('motacongviec', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Nội Dung Công Việc')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nhanvien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qlns.nhanvien', verbose_name='Nhân Viên Áp Dụng')),
                ('phongban', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qlns.phongban', verbose_name='Phòng Ban')),
            ],
            options={
                'verbose_name': 'MÔ TẢ CÔNG VIỆC',
                'verbose_name_plural': 'MÔ TẢ CÔNG VIỆC',
            },
        ),
    ]