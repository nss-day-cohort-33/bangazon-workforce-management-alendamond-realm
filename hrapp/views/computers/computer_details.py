import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Computer, Employee
from hrapp.models import model_factory
from ..connection import Connection

def get_computer(computer_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Employee)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.manufacturer,
            c.model,
            c.purchase_date,
            c.decommission_date
        FROM hrapp_computer c
        WHERE c.id = ?
        """, (computer_id,))

        return db_cursor.fetchone()


def computer_details(request, computer_id):
    if request.method == 'GET':
        computer = get_computer(computer_id)
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Computer)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                t.id,
                t.computer_id,
                t.employee_id,
                e.id employee_id,
                e.first_name,
                e.last_name,
                t.unassigned_date
            FROM hrapp_employeecomputer t
            LEFT JOIN hrapp_employee e ON e.id = t.employee_id
            """)

            data_set = db_cursor.fetchall()
            context = {
                'computer': computer,
                'employees': data_set
            }
        template_name = 'computer/computer_details.html'
        return render(request, template_name, context)
