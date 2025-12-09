from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer,json
from .serializers import task_serilizer
from .models import todolist
#fbv:
@api_view(['GET','POST','PUT','DELETE'])
def todolist_op(request,id=None):
    if request.method =='GET':
        if id is not None:
            task_data=todolist.objects.get(id=id)
            serializer_data=task_serilizer(task_data)
            return Response(serializer_data.data)
        task_data=todolist.objects.all()
        serializer_data=task_serilizer(task_data,many=True)
        return Response(serializer_data.data)
    
    if request.method =='POST':
        serializer_data=task_serilizer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response({"msg":"added"})
        json_data = JSONRenderer().render(serializer_data.errors)
        return Response(json_data,content_type='application/json')
    
    if request.method =='PUT':
        task_data=todolist.objects.get(id=id)
        serializer_data=task_serilizer(instance=task_data,data=request.data,partial=True)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response({"msg":"updated"})
        json_data = JSONRenderer().render(serializer_data.errors)
        return Response(json_data,content_type='application/json')
    
    if request.method =='DELETE':
        task_data=todolist.objects.get(id=id)
        task_data.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)
    