from django.db import models

# Create your models here.
class TodoList(models.Model):
    item=models.CharField(max_length=50)
    checkbox=models.BooleanField()


    def __str__(self):
        return self.item