# Generated by Django 4.2 on 2023-04-28 14:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0017_alter_service_profile_projectimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="category",
            field=models.CharField(
                choices=[
                    (1, "Backend"),
                    (2, "Mobile"),
                    (3, "Frontend"),
                    (4, "Desktop App"),
                ],
                default=1,
                max_length=1,
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="client",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="release_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
