from django.db import models


class UserAccount(models.Model):
    user_name = models.CharField(max_length=10)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.user_name


class TaskCreate(models.Model):
    task_title = models.CharField(max_length=50)
    task_text = models.CharField(max_length=300)
    date = models.DateField()

    def __str__(self):
        return self.task_title
