import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse

from hrapp.models import TrainingProgram
from hrapp.models import model_factory
from ..connection import Connection


@login_required
def training_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:

            conn.row_factory = model_factory(TrainingProgram)

            db_cursor = conn.cursor()
            db_cursor.execute("""
            select
                t.id,
                t.name,
                t.description,
                t.start_date,
                t.end_date,
                t.max_num
            from hrapp_trainingprogram t
            """)

            all_trainings = db_cursor.fetchall()

        template = 'training_programs/training_list.html'
        context = {
            'all_trainings': all_trainings
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_trainingprogram
            (
                name, description, start_date,
                end_date, max_num
            )
            VALUES (?, ?, ?, ?, ?)
            """,
                              (form_data['name'], form_data['description'],
                               form_data['start_date'], form_data['end_date'],
                                  form_data["max_num"]))

        return redirect(reverse('hrapp:training_list'))
