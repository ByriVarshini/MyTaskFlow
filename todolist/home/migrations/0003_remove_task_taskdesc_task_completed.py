# Generated by Django 5.1.4 on 2025-01-31 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_title_task_tasktitle_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='taskdesc',
        ),
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
