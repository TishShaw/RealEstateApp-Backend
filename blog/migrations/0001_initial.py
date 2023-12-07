# Generated by Django 4.2.7 on 2023-12-07 22:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=255, null=True)),
                ("content", models.TextField(null=True)),
                ("authour", models.CharField(max_length=255, null=True)),
                ("slug", models.SlugField(blank=True, unique=True)),
                ("tags", models.CharField(max_length=255, null=True)),
                ("date_added", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]