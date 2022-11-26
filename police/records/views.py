from django.shortcuts import render
from .models import Arrest, Report
import csv
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.db.models import Q
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
def index(request):
    return render (request, 'records/home.html')

# record creation view


def report_list(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    report_list = Report.objects.filter(
        Q(victim_id__icontains=q) |
        Q(victim_name__icontains=q) |
        Q(date__icontains=q) 


    )
    context = {
        'report_list': report_list,
        
    }
    return render(request, 'records/report_list.html', context)

class ReportCreateView( CreateView):
    model = Report
    template_name = 'records/new_report.html'
    fields=('victim_name','victim_id','crime_type','crime_location','description')
    success_url = reverse_lazy('report_list')

def arrest_list(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    arrest_list = Arrest.objects.filter(
        Q(suspect_id__icontains=q) 
       
    )
    context = {
        'arrest_list': arrest_list,
        
    }
    return render(request, 'records/arrest_list.html', context)

class ArrestCreateView( CreateView):
    model = Arrest
    template_name = 'records/new_arrest.html'
    fields=('suspect_name','suspect_id','crime_type','crime_location','description')
    success_url = reverse_lazy('arrest_list')