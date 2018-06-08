from rest_framework import serializers
from .models import chatData

class chatData_serializer(serializers.ModelSerializer):
    class Meta:
        model = chatData
        fields = ('group_name', 'username', 'text_content')