# Generated by Django 4.2 on 2023-04-26 13:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0009_alter_profile_birthday"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="birthday",
            field=models.DateField(blank=True, null=True),
        ),
    ]
