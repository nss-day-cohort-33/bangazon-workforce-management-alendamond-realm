from django.db import models
from .training_program import TrainingProgram
from .employee import Employee

class EmployeeTrainingProgram(models.Model):
    """
    Creates the join table for the many to many relationship between employees and training programs
    """

    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    training_program = models.ForeignKey("TrainingProgram", on_delete=models.CASCADE)
