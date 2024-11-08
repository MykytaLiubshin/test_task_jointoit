from django.db import models
from users.models import User

# Create your models here.


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateTimeField()
