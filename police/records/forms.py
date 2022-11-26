from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Arrest, Report
# Create your forms here.

class ItemForm(forms.ModelForm):
    class Meta:
        model = Arrest
        fields=('suspect_name','suspect_id','crime_type','crime_location','description')

class ReportForm(forms.Form):
    class Meta:
        model= Report
        fields=('victim_name','victim_id','crime_type','crime_location','description')