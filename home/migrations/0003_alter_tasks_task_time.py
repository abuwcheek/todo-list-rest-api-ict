# Generated by Django 5.1.1 on 2024-12-10 16:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_tasks_task_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='task_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 12, 11, 0, 12, 40, 987605), null=True),
        ),
    ]
