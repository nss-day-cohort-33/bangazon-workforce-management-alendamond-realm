import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Department, Employee
from hrapp.models import model_factory
from ..connection import Connection


def create_department(cursor, row):
    _row = sqlite3.Row(cursor, row)

    department = Department()
    department.id = _row["id"]
    department.dept_name = _row["dept_name"]
    department.budget = _row["budget"]

    # Note: You are adding a blank employees list to the department object
    # This list will be populated later (see below)

    employee = Employee()
    employee.id = _row["employee_id"]
    employee.first_name = _row["first_name"]
    employee.Last_name = _row["last_name"]

    department.employees = employee
    # Return a tuple containing the department and the
    # employee built from the data in the current row of
    # the data set
    return (department, employee,)



def get_department(department_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_department

        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            d.id,
            d.dept_name,
            d.budget,
            e.id employee_id,
            e.first_name,
            e.last_name,
            e.department_id
        FROM hrapp_department d
        join hrapp_employee e on d.id = e.department_id
        WHERE d.id = ?
        """, (department_id,))

        return db_cursor.fetchone()



@login_required
def department_details(request, department_id):
    if request.method == 'GET':
        department_details = get_department(department_id)

        template = 'departments/department_details.html'
        context = {
            "department_details": department_details
            }

        return render(request, template, context)

