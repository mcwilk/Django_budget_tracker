# Generated by Django 2.2.12 on 2020-05-08 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0010_expense_date2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='date2',
        ),
    ]