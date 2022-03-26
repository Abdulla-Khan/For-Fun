from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=20,null=True)
    image = models.CharField(max_length=2000,null=True)
    def __str__(self):
        return self.title   