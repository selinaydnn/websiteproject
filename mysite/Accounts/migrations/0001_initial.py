# Generated by Django 4.2.7 on 2023-12-31 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("signin", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Login",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "signin",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="signin.signin"
                    ),
                ),
            ],
        ),
    ]