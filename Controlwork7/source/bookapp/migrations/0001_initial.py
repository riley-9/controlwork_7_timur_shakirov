# Generated by Django 4.1.7 on 2023-02-25 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Entry",
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
                ("author", models.CharField(max_length=120, verbose_name="Author")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("text", models.TextField(max_length=1000, verbose_name="Text")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("active", " Активно"), ("blocked", "Заблокированно")],
                        default="active",
                        max_length=10,
                        verbose_name="Status",
                    ),
                ),
            ],
        ),
    ]