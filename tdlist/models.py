from django.db import models
from datetime import timezone
# Create your models here.
class todolist(models.Model):
    task= models.CharField(max_length=200)
    is_completed= models.BooleanField(default=False)

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
