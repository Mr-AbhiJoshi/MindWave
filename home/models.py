from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField(default='No description provided')
    date = models.DateField(default=datetime.now)
    
    def __str__(self):
        return self.name