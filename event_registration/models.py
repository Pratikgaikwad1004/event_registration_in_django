from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models import deletion

class userEvent(models.Model):
    event_id = models.AutoField(primary_key=True)
    reguser = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    image = models.TextField(max_length=100)
    heading = models.CharField(max_length=100)
    day = models.CharField(max_length=2)
    month = models.CharField(max_length=3)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.heading
