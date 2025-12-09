from tdlist.models import *
from rest_framework import serializers

class task_serilizer(serializers.ModelSerializer):
    class Meta:
        model=todolist
        fields="__all__"