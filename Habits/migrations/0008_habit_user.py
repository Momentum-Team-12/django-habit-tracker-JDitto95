# Generated by Django 4.0.4 on 2022-05-25 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Habits', '0007_alter_record_habit'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='habit', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
