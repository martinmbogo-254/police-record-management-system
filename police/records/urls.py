from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from .views import index, ReportCreateView, ArrestCreateView,arrest_list,report_list

urlpatterns = [
    path('', views.index, name='home'),
    path('report/new', ReportCreateView.as_view(), name='add_report'),
    path('arrest/new', ArrestCreateView.as_view(), name='add_arrest'),
    path('arrest/list', views.arrest_list, name='arrest_list'),
    path('report/list', views.report_list, name='report_list'),




]