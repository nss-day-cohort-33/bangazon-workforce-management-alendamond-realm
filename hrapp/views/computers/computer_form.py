import sqlite3
from django.shortcuts import render
from hrapp.models import Computer
from hrapp.models import model_factory
from ..connection import Connection
from hrapp.models import Employee

def get_computers():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Computer)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
        c.id,
        c.manufacturer,
        c.model,
        c.purchase_date,
        c.decommission_date
        FROM hrapp_computer c;
        """)

        return db_cursor.fetchall()

def get_employee():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Employee)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            e.id,
            e.first_name,
            e.last_name
        from hrapp_employee e
        """)

        return db_cursor.fetchall()

def computer_form(request):
    if request.method == 'GET':
        employees = get_employee()
        template = 'computer/computer_form.html'
        context = {
            'all_employees': employees
        }

        return render(request, template, context)



