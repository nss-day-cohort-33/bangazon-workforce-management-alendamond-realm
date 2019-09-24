from django.db import models
from django.urls import reverse

class Department(models.Model):

    dept_name = models.CharField(max_length = 100)
    budget = models.IntegerField()

    class Meta:
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")

    def get_absolute_url(self):
        return reverse("department_details", kwargs={"pk": self.pk})