from django.db import models
import uuid

# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    constituency = models.CharField(max_length=100)

class Report (models.Model):
    report_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    victim_name = models.CharField(max_length=100)
    victim_id = models.IntegerField(max_length=8)
    crime_type = models.CharField(max_length=100)
    crime_location = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=100)

class Arrest(models.Model):
    arrest_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    suspect_name = models.CharField(max_length=100)
    suspect_id = models.IntegerField(max_length=8)
    date = models.DateTimeField(auto_now_add=True)    
    crime_type = models.CharField(max_length=100)
    crime_location = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
