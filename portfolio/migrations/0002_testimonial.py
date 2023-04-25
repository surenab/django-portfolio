# Generated by Django 4.2 on 2023-04-25 12:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Testimonial",
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
                ("name", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=100)),
                ("text", models.CharField(max_length=250)),
                (
                    "image",
                    models.ImageField(upload_to="portfolio/images/testimonials/"),
                ),
            ],
        ),
    ]
