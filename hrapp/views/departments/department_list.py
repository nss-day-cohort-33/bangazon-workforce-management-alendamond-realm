import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from hrapp.models import Department, Employee
from hrapp.models import model_factory
from ..connection import Connection
from django.contrib.auth.decorators import login_required


def create_department(cursor, row):
    _row = sqlite3.Row(cursor, row)

    department = Department()
    department.id = _row["department_id"]
    department.dept_name = _row["dept_name"]
    department.budget = _row["budget"]

    # Note: You are adding a blank employees list to the department object
    # This list will be populated later (see below)
    department.employees = []

    employee = Employee()
    employee.id = _row["employee_id"]
    employee.first_name = _row["first_name"]
    employee.Last_name = _row["last_name"]
    employee.department_id = _row["department_id"]


    # Return a tuple containing the department and the
    # employee built from the data in the current row of
    # the data set
    return (department, employee,)


@login_required
def department_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:

            conn.row_factory = create_department

            db_cursor = conn.cursor()
            db_cursor.execute("""
            select
                d.id dept_id,
                d.dept_name,
                d.budget,
                e.id employee_id,
                e.first_name,
                e.last_name,
                e.department_id
            from hrapp_department d
            join hrapp_employee e on d.id = e.department_id
            """)

            all_departments = db_cursor.fetchall()

        #Start with empty dictionary
        department_groups = {}

        # Iterate the list of tuples
        for(department, employee) in all_departments:

            # If the dictionary does have a key of the current
            # department 'id' value, add the key and set the
            # value to the current library
            if department.id not in department_groups:
                department_groups[department.id] = department
                department_groups[department.id].employees.append(employee)

            # If the key does exist, just append the current employee
            # to the list of employees for the current department

            else:
                department_groups[department.id].employees.append(employee)

        template = 'departments/department_list.html'
        context = {
            'all_departments': department_groups.values()
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_department
            (
                dept_name, budget
            )
            VALUES (?, ?)
            """,
            (form_data['dept_name'], form_data['budget']))

        return redirect(reverse('hrapp:department_list'))