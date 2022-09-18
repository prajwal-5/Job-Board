from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    location = models.CharField(max_length=250)
    deadline = models.DateField()
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    is_archieved = models.BooleanField(default=False)
    people = models.ManyToManyField(get_user_model())


