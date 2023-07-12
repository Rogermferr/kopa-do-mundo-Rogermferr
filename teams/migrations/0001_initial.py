# Generated by Django 4.2.1 on 2023-06-01 15:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Team",
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
                ("name", models.CharField(max_length=30)),
                ("titles", models.PositiveIntegerField(default=0, null=True)),
                ("top_scorer", models.CharField(max_length=50)),
                ("fifa_code", models.CharField(max_length=3, unique=True)),
                ("first_cup", models.DateField(null=True)),
            ],
        ),
    ]
