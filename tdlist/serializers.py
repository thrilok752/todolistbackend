from tdlist.models import *
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
class task_serilizer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=todolist
        fields = ['id', 'user', 'task', 'is_completed', 'date_created']
        

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        # Fields you want to allow during registration
        fields = ['id', 'email', 'username', 'password']

