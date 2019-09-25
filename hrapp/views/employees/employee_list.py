import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from hrapp.models import Employee
from ..connection import Connection
from hrapp.models import model_factory
from django.contrib.auth.decorators import login_required


@login_required
def employee_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Employee)
            db_cursor = conn.cursor()

            # TODO: Add to query: e.department,
            db_cursor.execute("""
            select
                e.id,
                e.first_name,
                e.last_name,
                e.start_date,
                e.is_supervisor
            from hrapp_employee e
            join auth_user u on e.user_id = u.id
            """)

            all_employees = db_cursor.fetchall()


    template = 'employees/employee_list.html'
    context = {
        'employees': all_employees
    }

    return render(request, template, context)

    return redirect(reverse('hrapp:employees'))

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                INSERT INTO hrapp_employee
                (
                    first_name, last_name, is_supervisor,
                    department_id, user_id
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (form_data['titlfirst_namee'], form_data['last_name'],
                    form_data['is_supervisor'], form_data['department_id'],
                    form_data["user_id"]))

            return redirect(reverse('hrapp:employees'))