import sqlite3
from django.shortcuts import render
from hrapp.models import Computer
from hrapp.models import model_factory
from ..connection import Connection

def get_computers():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Computer)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
        c.id,
        c.make,
        c.purchase_date,
        c.decommission_date
        FROM hrapp_computer c;
        """)

        return db_cursor.fetchall()


def computer_form(request):
    if request.method == 'GET':
        computer = get_computers()
        template = 'computer/computer_form.html'
        context = {
            'computer_form': computer
        }

        return render(request, template, context)

