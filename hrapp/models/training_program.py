from django.db import models
from django.urls import reverse

class TrainingProgram(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    max_num = models.IntegerField()

    class Meta:
        verbose_name = ("Training Program")
        verbose_name_plural = ("Training Program")
    def __str__(self):
        return f"{self.name} {self.description}"

    def get_absolute_url(self):
        return reverse("training_program_details", kwargs={"pk": self.pk})

