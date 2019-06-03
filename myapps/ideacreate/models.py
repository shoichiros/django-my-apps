from django.db import models


class FirstWord(models.Model):
    first_word = models.CharField(max_length=10)

    def __str__(self):
        return self.first_word


class SecondWord(models.Model):
    second_word = models.CharField(max_length=10)

    def __str__(self):
        return self.second_word


class ThirdWord(models.Model):
    third_word = models.CharField(max_length=10)

    def __str__(self):
        return self.third_word
