from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    
    #we do this to provide a human readable name for the object
    def __str__(self):
        return self.title
    
    