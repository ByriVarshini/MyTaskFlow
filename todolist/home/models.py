from django.db import models


# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')
    def __str__(self):
        return self.taskTitle