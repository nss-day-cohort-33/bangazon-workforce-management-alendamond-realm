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
    path('employees/<int:employee_id>/form', employee_edit_form, name='employee_edit_form'),
    path('employees/', employee_list, name='employee_list'),
    path('training_programs/', training_list, name='training_list'),
    path('employees/form', employee_form, name='employee_form'),
    path('employees/<int:employee_id>/', employee_details, name='employee'),
    path('training_programs/form', training_form, name='training_form'),
    path('training_programs/<int:training_id>', training_details, name='training_details'),
    path('training_programs/<int:training_id>/form', training_edit_form, name='training_edit_form'),
    path('departments/', department_list, name='department_list'),
    path('departments/<int:department_id>/', get_department_and_employees, name='department_details'),
    path('^department/form$', department_form, name='department_form'),
    path('computers/', computer_list, name='computer_list'),
    path('computer/form', computer_form, name='computer_form'),
    path('computer/<int:computer_id>/', computer_details, name='computer')

]


