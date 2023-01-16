from django.urls import path,reverse
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from .views import index, ReportCreateView, Arrest_create,IncidenceDetail,arrest_list,report_list, login_request,logout_request,report,arrest_report

urlpatterns = [
    path('', views.index, name='home'),
    path('report/new', ReportCreateView.as_view(), name='add_report'),
    # path('arrest/new', ArrestCreateView.as_view(), name='add_arrest'),
    path('arrest/list', views.arrest_list, name='arrest_list'),
    path('report/list', views.report_list, name='report_list'),
    path('login', auth_views.LoginView.as_view(template_name='records/login.html'), name='login'),
    path('reports_download', views.report , name='reports-download'),
    path('arrest_download', views.arrest_report , name='arrest-download'),
    path("logout", views.logout_request, name= "logout"),
    path('incidence/<int:pk>/',views.IncidenceDetail, name='detail' ),
    path('incidence/<int:pk>/new_arrest',views.Arrest_create, name='add_arrest' ),


]
