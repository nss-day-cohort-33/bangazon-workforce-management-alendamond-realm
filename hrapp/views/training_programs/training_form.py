import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .training_details import get_training
from ..connection import Connection


@login_required
def training_form(request):
    if request.method == 'GET':
        template = 'training_programs/training_form.html'
        return render(request, template)

@login_required
def training_edit_form(request, training_id):

    if request.method == 'GET':
        training = get_training(training_id)
        template = 'training_programs/training_form.html'
        context = {
            'training': training,
        }

        return render(request, template, context)