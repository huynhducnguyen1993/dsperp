from import_export import resources
from cdqttb.models import *


class ThongbaoResource(resources.ModelResource):
    class Meta:
        model = Thongbao
        exclude = ('imported',)