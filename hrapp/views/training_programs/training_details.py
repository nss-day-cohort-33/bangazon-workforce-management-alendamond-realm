import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import TrainingProgram
from hrapp.models import model_factory
from ..connection import Connection


def get_training(training_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(TrainingProgram)
        db_cursor = conn.cursor()

        db_cursor.execute("""
          SELECT
                tp.id,
                tp.title,
                tp.description,
                tp.start_date,
                tp.end_date,
                tp.capacity
            FROM hrapp_trainingprogram tp
            WHERE tp.id = ?
            """, (training_id,))

        return db_cursor.fetchone()

@login_required
def training_details(request, training_id):
    if request.method == 'GET':
        training = get_training(training_id)
        template = 'training_programs/training_details.html'
        context = {
            'training': training
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE hrapp_trainingprogram
                SET title = ?,
                    description = ?,
                    start_date = ?,
                    end_date = ?,
                    capacity = ?
                WHERE id = ?
                """,
                (
                    form_data['title'], form_data['description'],
                    form_data['start_date'], form_data['end_date'],
                    form_data['capacity'], training_id
                ))
            return redirect(reverse('hrapp:training_list'))


    # if request.method == 'POST':
    #     form_data = request.POST

        # Check if this POST is for deleting a book
        #
        # Note: You can use parenthesis to break up complex
        #       `if` statements for higher readability
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM hrapp_trainingprogram
                WHERE id = ?
                """, (training_id,))

            return redirect(reverse('hrapp:training_list'))


