# Generated by Django 3.2.3 on 2021-07-16 14:26

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qlns', '0009_auto_20210716_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giaichi',
            name='noidunggiaichi',
            field=ckeditor_uploader.fields.RichTextUploadingField(default="<table align='center' border='1' cellpadding='1' cellspacing='1' class='hover' style='height:288px; width:786px'><caption>Nội Dung Giải Chi</caption><tbody><tr><td><h2>STT</h2></td><td><h2>SBN</h2></td><td><h2>Nội Dung H&agrave;ng H&oacute;a</h2></td><td><h2>Số lượng</h2></td><td><h2>Đơn Gi&aacute;</h2></td><td><h2>Th&agrave;nh Tiền</h2></td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td colspan='5' rowspan='1'><span style='color:#3498db'><strong>Tổng</strong></span></td><td>&nbsp;</td></tr></tbody></table><p>&nbsp;</p><p>&nbsp;</p>"),
        ),
    ]
