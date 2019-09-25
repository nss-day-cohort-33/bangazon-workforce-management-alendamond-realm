import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Employee
from hrapp.models import model_factory
from ..connection import Connection


def get_employee(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Employee)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            select
                e.id,
                e.first_name,
                e.last_name,
                e.start_date,
                e.is_supervisor
            from hrapp_employee e
            join auth_user u on e.user_id = u.id
            where e.id = ?
        """, (employee_id,))

        return db_cursor.fetchone()

@login_required
def employee_details(request, employee_id):
    if request.method == 'GET':
        employee = get_employee(employee_id)

        template = 'employees/details.html'
        context = {
            'employee': employee
        }

        return render(request, template, context)