import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrapp.models import Department
from hrapp.models import model_factory
from ..connection import Connection
from .department_details import get_department

def get_departments():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Department)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            d.id,
            d.dept_name,
            d.budget
        from hrapp_department d
        """)

        return db_cursor.fetchall()

@login_required
def department_form(request):
    if request.method == 'GET':
        departments = get_departments()
        template = 'departments/department_form.html'
        context = {
            'all_departments': departments
        }

        return render(request, template, context)

