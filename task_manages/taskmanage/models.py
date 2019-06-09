from django.db import models


class Task(models.Model):
    task_title = models.CharField(max_length=50)
    task_text = models.CharField(max_length=300)
    date = models.DateField()

    def __str__(self):
        return self.task_title
