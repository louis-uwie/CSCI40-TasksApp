from django.db import models
from django.utils import timezone
    
    #TODO: create profile class for proxy

class Task(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=False)
    
    def is_overdue(self):
        return timezone.localtime(timezone.now()).date() > self.due_date.date()
