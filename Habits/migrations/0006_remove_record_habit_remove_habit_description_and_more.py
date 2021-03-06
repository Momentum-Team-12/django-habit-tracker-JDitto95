# Generated by Django 4.0.4 on 2022-05-20 14:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Habits', '0005_remove_record_time'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='record',
            name='Habit',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='description',
        ),
        migrations.RemoveField(
            model_name='record',
            name='created_at',
        ),
        migrations.AddField(
            model_name='record',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AddConstraint(
            model_name='record',
            constraint=models.UniqueConstraint(fields=('habit', 'date'), name='once_per_day'),
        ),
    ]
