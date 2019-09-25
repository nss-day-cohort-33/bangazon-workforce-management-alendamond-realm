import sqlite3
from hrapp.models import Computer
from hrapp.models import model_factory
from ..connection import Connection
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect


def computer_list (request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
                conn.row_factory = sqlite3.Row
                db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
        c.id,
        c.make,
        c.purchase_date,
        c.decommission_date
        FROM hrapp_computer c;
        """)

        all_computers = db_cursor.fetchall()

        template = 'computer/computer_list.html'
        context = {
                'all_computers': all_computers
            }
        return render(request, template, context)
    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_computer
            (
                make, purchase_date, decommission_date
            )
            VALUES (?, ?, ?)
            """,
            (form_data['make'], form_data['purchase_date'], form_data['decommission_date']))

        return redirect(reverse('hrapp:computer_list'))
