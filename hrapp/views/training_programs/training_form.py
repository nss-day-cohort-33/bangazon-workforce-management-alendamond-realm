import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..connection import Connection


@login_required
def training_form(request):
    if request.method == 'GET':
        template = 'training_programs/training_form.html'
        return render(request, template)
