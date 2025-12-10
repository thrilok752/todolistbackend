from django.db import models
from datetime import timezone
from todo_backend import settings
# Create your models here.
class todolist(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
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

# tdlist/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # CRITICAL: Define email as unique and required
    email = models.EmailField(
        unique=True,
        max_length=254,
        verbose_name='email address',
        blank=False,
        null=False,
    )
    # The AbstractUser provides username, password, first_name, last_name, etc.
    
    # Set the email field as the primary unique identifier for Djoser/Django
    # Note: username is still required by AbstractUser unless you also customize the manager.
    # We will keep username for compatibility but make email primary.
    
    def __str__(self):
        return self.email
