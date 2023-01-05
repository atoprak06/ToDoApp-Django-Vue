from django.shortcuts import redirect
from .serializer import TodoSerializer
from .models import Todo
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def TodoView(request):
    if request.method == 'GET':
        queryset = Todo.objects.all()        
        serializer = TodoSerializer(queryset,many=True)       
        return Response(serializer.data)
    
    if request.method == 'POST':
        Todo.objects.create(**request.data)
        return redirect('todo')
        


@api_view(['GET', 'PUT', 'DELETE'])
def TodoDetailView(request,id):
    if request.method == 'GET':
        queryset = Todo.objects.get(id=id)        
        serializer = TodoSerializer(queryset,many=False)        
        return Response(serializer.data)
    
    if request.method == 'PUT':      
        queryset = Todo.objects.filter(id=id).update(**request.data)        
        return Response(request.data)
    
    if request.method == 'DELETE':      
        queryset = Todo.objects.filter(id=id).delete()     
        return Response('Object is deleted')

   
