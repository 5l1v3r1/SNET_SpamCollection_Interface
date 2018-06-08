from django.shortcuts import render
from rest_framework import viewsets
from .models import chatData
from .serializers import chatData_serializer

class chatdataView(viewsets.ModelViewSet):
    queryset = chatData.objects.all()
    serializer_class = chatData_serializer