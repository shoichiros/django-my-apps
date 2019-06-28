from django.db import models


class Test(models.Model):
    username = models.CharField(max_length=10)
    my_text = models.CharField(max_length=50)

    def __str__(self):
        return self.username
