# Generated by Django 4.2.7 on 2024-01-03 05:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_alter_customuser_managers"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="user_name",
        ),
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
