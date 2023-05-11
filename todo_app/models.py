from django.db import models
from django.conf import settings
# Create your models here.

class TodoItem(models.Model):
    
# Todo Item Model
    
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="todo_item")

   

    def __str__(self):
        return self.name