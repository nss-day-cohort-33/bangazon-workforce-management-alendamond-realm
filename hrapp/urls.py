from django.urls import path
from django.conf.urls import include
from hrapp import views
from .views import *

app_name = 'hrapp'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('training_programs/', training_list, name='training_list'),
    path('training_programs/form', training_form, name='training_form'),
]
