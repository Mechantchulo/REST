from rest_framework import serializers
from .models import Todo #impor the model

#create a serializer class

class TodoSerializer(serializers.ModelSerializer):
    #this class will be used to serialize the Todo model
    class Meta:
        model = Todo #the model to be serilaized
        fields = ('id', 'title', 'body',) #the fields to be serialized