# Generated by Django 4.2 on 2023-04-26 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0012_skill_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="profile",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="portfolio.profile",
            ),
            preserve_default=False,
        ),
    ]