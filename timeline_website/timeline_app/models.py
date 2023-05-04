from django.db import models

# Create your models here.
class Timeline(models.Model):
    timeline_id = models.BigAutoField(primary_key=True)
    timeline_name = models.CharField(max_length=50)
    
class Event(models.Model):
    timeline_id = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    event_id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)