from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer,json
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import task_serilizer
from .models import todolist
#fbv:
@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def todolist_op(request,id=None):
    if request.method =='GET':
        if id is not None:
            try:
                task_data=todolist.objects.get(id=id,user=request.user)
            except todolist.DoesNotExist:
                return Response({'details':"not found or no task"},status= status.HTTP_404_NOT_FOUND)
            serializer_data=task_serilizer(task_data)
            return Response(serializer_data.data)
        task_data=todolist.objects.filter(user=request.user).order_by('-date_created')
        serializer_data=task_serilizer(task_data,many=True)
        return Response(serializer_data.data)
    
    if request.method =='POST':
        data=request.data.copy()
        data['user']=request.user.id
        serializer_data=task_serilizer(data=data)
        if serializer_data.is_valid():
            serializer_data.save(user=request.user)
            return Response({"msg":"added"},status=status.HTTP_201_CREATED)
        json_data = JSONRenderer().render(serializer_data.errors)
        return Response(json_data,content_type='application/json')
    
    if request.method =='PUT':
        
        try:
            task_data=todolist.objects.get(id=id,user=request.user)
        except todolist.DoesNotExist:
            return Response({'details':"not found or no task"},status= status.HTTP_404_NOT_FOUND)
        
        data=request.data.copy()
        data['user']=request.user.id
        
        serializer_data=task_serilizer(instance=task_data,data=data,partial=True)
        if serializer_data.is_valid():
            serializer_data.save(user=request.user)
            return Response({"msg":"updated"})
        json_data = JSONRenderer().render(serializer_data.errors)
        return Response(json_data,content_type='application/json')
    
    if request.method =='DELETE':
        
        try:
            task_data=todolist.objects.get(id=id,user=request.user)
        except todolist.DoesNotExist:
            return Response({'details':"not found or no task"},status= status.HTTP_404_NOT_FOUND)
        task_data.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)
    
    return Response({"detail": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    