# Generated by Django 3.1.2 on 2020-10-15 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Human",
            fields=[
                (
                    "id",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
                ("name", models.CharField(max_length=1024)),
                ("gender", models.IntegerField()),
                ("height", models.IntegerField()),
                ("birth_year", models.CharField(max_length=1024)),
                ("mass", models.IntegerField()),
                ("home_planet", models.CharField(max_length=1024)),
            ],
        ),
    ]