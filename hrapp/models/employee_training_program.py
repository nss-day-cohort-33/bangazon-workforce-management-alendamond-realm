from django.db import models

class EmployeeTrainingProgram(models.Model):
    """
    Creates the join table for the many to many relationship between employees and training programs
    """

    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    training_program = models.ForeignKey("Training Program", on_delete=models.CASCADE)
