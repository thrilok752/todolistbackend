from django.db import models
from datetime import timezone
from django.contrib.auth.models import User
# Create your models here.
class todolist(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    task= models.CharField(max_length=200)
    is_completed= models.BooleanField(default=False)
    date_created= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task

# class todolist(models.Model):
#     task= models.TextField(max_length=200)
#     completed= models.BooleanField(default=False)
#     task_added_time= models.DateTimeField(auto_now=True,auto_now_add=True)
#     task_completed_time= models.DateTimeField(null=True,blank=True)
    
#     def save(self, *args, **kwargs):
#         if not self.completed and self.task_completed_time:
#             self.task_completed_time=None
#         elif self.completed and not self.task_completed_time:
#             self.task_completed_time=timezone.now()
        
        
#         super().save(*args, **kwargs)
