from django.db import models
from datetime import datetime, timedelta


class Tasks(models.Model):
     title = models.CharField(max_length=300)
     complete = models.BooleanField(default=False)
     task_time = models.DateTimeField(null=True, blank=True, default=datetime.now() + timedelta(hours=6)) 
     created = models.DateTimeField(auto_now_add=True)
     updated = models.DateTimeField(auto_now=True)


     def __str__(self):
          return self.title