# Generated by Django 3.1.3 on 2020-12-07 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cw_22', '0003_student_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='book',
        ),
    ]