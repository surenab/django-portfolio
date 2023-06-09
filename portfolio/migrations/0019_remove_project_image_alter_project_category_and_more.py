# Generated by Django 4.2 on 2023-04-28 14:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0018_project_category_project_client_project_release_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="image",
        ),
        migrations.AlterField(
            model_name="project",
            name="category",
            field=models.CharField(
                choices=[
                    ("B", "Backend"),
                    ("M", "Mobile"),
                    ("F", "Frontend"),
                    ("D", "Desktop App"),
                ],
                default=1,
                max_length=1,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
