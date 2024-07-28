# Generated by Django 5.0.4 on 2024-07-28 20:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='social.profile'),
            preserve_default=False,
        ),
    ]
