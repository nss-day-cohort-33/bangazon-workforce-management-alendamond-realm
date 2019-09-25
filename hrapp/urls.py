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
    # path('^employee/form$', employee_form, name='employee_form')
    path('computer/', computer_list, name='computer_list'),
    path('computer/form', computer_form, name='computer_form')
]


