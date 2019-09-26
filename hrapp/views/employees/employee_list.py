import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from hrapp.models import Employee, Department
from ..connection import Connection
from hrapp.models import model_factory
from django.contrib.auth.decorators import login_required


@login_required
def employee_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Employee)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                e.id,
                e.first_name,
                e.last_name,
                e.start_date,
                e.is_supervisor,
                d.dept_name,
                d.budget,
                d.id department_id
            from hrapp_employee e
            join hrapp_department d on e.department_id = d.id
            """)

            all_employees = db_cursor.fetchall()


        template = 'employees/employee_list.html'
        context = {
            'employees': all_employees
        }

        return render(request, template, context)

    elif request.method == 'POST':
      form_data = request.POST


    with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_employee
            (
                first_name, last_name, start_date, is_supervisor, department_id
            )
            VALUES (?, ?, ?, ?)
            """,
            (form_data['first_name'], form_data['last_name'],  form_data["start_date"], form_data["is_supervisor"], form_data["department_id"] ))

    return redirect(reverse('hrapp:employee_list'))
