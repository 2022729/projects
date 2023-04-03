from django.db import models

# Create your models here.
class Task(models.Model):
    name=models.TextField(max_length=50)
    priority=models.IntegerField()
    date=models.DateTimeField()
    def __str__(self):
        return self.name

