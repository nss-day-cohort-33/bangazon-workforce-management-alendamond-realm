from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url
from hrapp.models import *
from hrapp import views
from .views import *
from django.conf.urls import url


app_name = 'hrapp'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
<<<<<<< HEAD
    # path('^employee/form$', employee_form, name='employee_form')
=======
    path('departments/', department_list, name='department_list'),
    path('departments/<int:department_id>/', department_details, name='department_details'),
    path('^department/form$', department_form, name='department_form'),
>>>>>>> master
    path('computer/', computer_list, name='computer_list'),
    path('computer/form', computer_form, name='computer_form')
]


