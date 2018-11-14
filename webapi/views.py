from django.shortcuts import render
from rest_framework import generics
from app.models import SysConfig
from webapi.apiSerializer import apiSerializers

# Create your views here.


class SysConfig(generics.ListAPIView):
    queryset = SysConfig.objects.all()
    serializer_class = apiSerializers
