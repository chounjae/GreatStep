# Generated by Django 5.1.4 on 2025-02-20 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visibility',
            field=models.BooleanField(default=False),
        ),
    ]
