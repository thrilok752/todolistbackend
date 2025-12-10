from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from tdlist.models import todolist,CustomUser
# --- TASK SERIALIZER (Left unchanged) ---
class task_serilizer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True) 
    class Meta:
        model = todolist
        fields = ['id', 'user', 'task', 'is_completed', 'date_created']
        
# --- USER CREATION SERIALIZER (CRITICAL FIX HERE) ---
class UserCreateSerializer(BaseUserCreateSerializer):
    # No custom email or validation needed here! 
    # The BaseUserCreateSerializer reads the unique=True directly from CustomUser model's Meta.
    
    class Meta(BaseUserCreateSerializer.Meta):
        # Point the serializer to the new model
        model = CustomUser 
        fields = ['id', 'email', 'username', 'password', 're_password']
        
        



