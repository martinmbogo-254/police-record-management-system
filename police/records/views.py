from django.shortcuts import render, get_object_or_404

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
@login_required(login_url='login')

def index(request):
    recent_arrests = Arrest.objects.order_by('date')[:5]
    recent_reports = Report.objects.order_by('date')[:5]

    arrests = Arrest.objects.all()
    reports = Report.objects.all()
    total_arrests = arrests.count()
    total_reports = reports.count()

    context={
        'total_arrests':total_arrests,
        'total_reports':total_reports,
        'recent_arrests':recent_arrests,
        'recent_reports':recent_reports
    }
    return render (request, 'records/home.html',context)

# record creation view

@login_required(login_url='login')

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

    # report details view
def IncidenceDetail(request, pk):
    incidence = Report.objects.get(id=pk)
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    arrest_list = Arrest.objects.filter(
        Q(suspect_id__icontains=q) |
        Q(suspect_name__icontains=q) |
        Q(date__icontains=q) 
       
    )
    context = {
        'incidence': incidence, 
        'arrest_list': arrest_list,
    }
    return render(request, 'records/incidence_detail.html', context)

# @login_required(login_url='login')
class ReportCreateView( CreateView):
    model = Report
    template_name = 'records/new_report.html'
    fields=('victim_name','victim_id','crime_type','crime_location','description')
    success_url = reverse_lazy('report_list')

@login_required(login_url='login')
def arrest_list(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    arrest_list = Arrest.objects.filter(
        Q(suspect_id__icontains=q) |
        Q(suspect_name__icontains=q) |
        Q(date__icontains=q) 
       
    )
    context = {
        'arrest_list': arrest_list,
        
    }
    return render(request, 'records/arrest_list.html', context)

# @login_required(login_url='login')
class ArrestCreateView( CreateView):
    model = Arrest
    template_name = 'records/new_arrest.html'
    fields=('suspect_name','suspect_id','crime_type','crime_location','description')
    success_url = reverse_lazy('arrest_list')


# login view

def login_request(request):
    if request.method=="POST":
        form =AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {{username}}")
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
        context ={
            'login_form': form
        }
        form = AuthenticationForm()
        return render(request=request,template_name='records/login.html',context=context)

# report download view

@login_required(login_url='login')
def report(request):
    response =HttpResponse(content_type ='text/csv')
    response['content-disposition'] = 'attachment; filename=Casesreport.csv'

    writer = csv.writer(response)

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    report_list = Report.objects.filter(
        Q(victim_id__icontains=q) |
        Q(victim_name__icontains=q) |
        Q(date__icontains=q) 


    )

    writer.writerow(['REPORT_ID','DATE','SUSPECT_NAME','SUSPECT_ID','CRIME_TYPE','CRIME_LOCATION','DESCRIPTION'])  

    for report_list in report_list:
        writer.writerow([report_list.report_id,report_list.date,report_list.victim_name,report_list.victim_id,report_list.crime_type,report_list.crime_location,report_list.description])

    return response

# arrest report download view

def arrest_report(request):
    response =HttpResponse(content_type ='text/csv')
    response['content-disposition'] = 'attachment; filename=Arrestsreport.csv'

    writer = csv.writer(response)

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    arrest_list = Arrest.objects.filter(
        Q(suspect_id__icontains=q) |
        Q(suspect_name__icontains=q) |
        Q(date__icontains=q) 


    )

    writer.writerow(['REPORT_ID','DATE','SUSPECT_NAME','VICTIM_ID','CRIME_TYPE','CRIME_LOCATION','DESCRIPTION'])  

    for arrest_list in arrest_list:
        writer.writerow([arrest_list.arrest_id,arrest_list.date,arrest_list.suspect_name,arrest_list.suspect_id,arrest_list.crime_type,arrest_list.crime_location,arrest_list.description])

    return response

# logout view

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('login')