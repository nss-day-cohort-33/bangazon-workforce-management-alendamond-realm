import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Department, Employee
from hrapp.models import model_factory
from ..connection import Connection




def employee_list():
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
            e.is_supervisor,
            e.department_id
        from hrapp_employee e
        """)

        return db_cursor.fetchall()


def get_department(department_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Department)

        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            d.id,
            d.dept_name,
            d.budget
        FROM hrapp_department d
        WHERE d.id = ?
        """, (department_id,))

        return db_cursor.fetchone()


def get_department_and_employees(request, department_id):
    if request.method == 'GET':
        employees = employee_list()
        department = get_department(department_id)


        template = 'departments/department_details.html'
        context = {
            'department': department,
            'all_employees': employees
        }

        return render(request, template, context)



# @login_required
# def department_details(request, department_id):
#     if request.method == 'GET':
#         department_details = get_department_and_employees(request, department_id)

#         template = 'departments/department_details.html'
#         context = {
#             "department_details": department_details
#             }

#         return render(request, template, context)

