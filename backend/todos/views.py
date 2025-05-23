from django.shortcuts import render
from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer



# Create your views here.

class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all() #get all the objects from the database
    serializer_class = TodoSerializer #use the serializer class to serialize the data
    
class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all() #get all the objects from the database
    serializer_class = TodoSerializer #use the serializer class to serialize the data
