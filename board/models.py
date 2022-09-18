from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from datetime import date, timedelta

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
    order = models.IntegerField(default=0, blank=True)


    @property
    def days_left(self):
        return self.deadline - date.today()


    @property
    def bg_class(self):
        if self.days_left > timedelta(days=21):
            return "success"
        elif self.days_left < timedelta(days=3):
            return "danger"
        elif self.days_left < timedelta(days=14):
            return "warning"
        else:
            return "secondary"

    
    class Meta:
        ordering = ['order', 'pk']


