from django.db import models
import uuid
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    constituency = models.CharField(max_length=100)

class Crime(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) :
        return self.name

class Report (models.Model):
    report_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    victim_name = models.CharField(max_length=100)
    victim_id = models.IntegerField(max_length=8)
    crime_type = models.ForeignKey(Crime,on_delete=models.CASCADE,null=True, blank=False)
    crime_location = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=100)
    # user = models.OneToOneField(User,on_delete=models.CASCADE,default=0)
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


    
   

class Arrest(models.Model):
    incidence = models.ForeignKey(Report, on_delete=models.CASCADE,blank=False, default=1)
    arrest_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    suspect_name = models.CharField(max_length=100)
    suspect_id = models.IntegerField(max_length=8)
    date = models.DateTimeField(auto_now_add=True)    
   
   