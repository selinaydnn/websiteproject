# Generated by Django 4.2.7 on 2024-01-01 22:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Accounts", "0002_alter_login_signin"),
        ("signin", "0002_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="SignIn",
        ),
    ]