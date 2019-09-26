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
                e.id,
                e.first_name,
                e.last_name,
                e.start_date,
                e.is_supervisor,
                d.dept_name,
                d.budget,
                d.id department_id,
                c.id computer_id,
                c.manufacturer,
                c.model,
                etp.employee_id,
                tp.id training_program_id,
                tp.title,
                tp.start_date training_start_date,
                tp.end_date
            from hrapp_employee e
            left join hrapp_department d on e.department_id = d.id
            left join hrapp_employeecomputer ec on e.id = ec.employee_id
            left join hrapp_computer c on c.id = ec.computer_id
            left join hrapp_employeetrainingprogram etp on e.id = etp.employee_id
            left join hrapp_trainingprogram tp on tp.id = etp.training_program_id
            where e.id = ?
        """, (employee_id,))

        return db_cursor.fetchone()

@login_required
def employee_details(request, employee_id):
    if request.method == 'GET':
        employee = get_employee(employee_id)

        template = 'employees/employee_details.html'
        context = {
            'employee': employee
        }

        return render(request, template, context)
