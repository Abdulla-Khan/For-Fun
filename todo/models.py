from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200,null=True)
    image = models.CharField(max_length=200,null=True)
    rent =  models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.title   