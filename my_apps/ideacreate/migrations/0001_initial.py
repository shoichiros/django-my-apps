# Generated by Django 2.1.5 on 2019-03-16 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_word', models.CharField(max_length=10)),
                ('second_word', models.CharField(max_length=10)),
                ('third_word', models.CharField(max_length=10)),
            ],
        ),
    ]