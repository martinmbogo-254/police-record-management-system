from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Arrest, Report
# Create your forms here.


class ReportForm(forms.Form):
    class Meta:
        model= Report
        fields=('victim_name','victim_id','crime_type','crime_location','description')


class ArrestForm(forms.ModelForm):

    class Meta:
        model = Arrest
        fields = ['suspect_name','suspect_id']