from rest_framework import serializers
from app.models import SysConfig


class apiSerializers(serializers.ModelSerializer):
    class Meta:
        model = SysConfig
        fields = ('id','Content','ConfigType','Updated')
