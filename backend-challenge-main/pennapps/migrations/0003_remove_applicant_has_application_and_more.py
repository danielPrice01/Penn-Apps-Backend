# Generated by Django 5.0.2 on 2024-02-11 07:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pennapps", "0002_applicant_has_application_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="applicant",
            name="has_application",
        ),
        migrations.AddField(
            model_name="applicant",
            name="application",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="applicant_application",
                to="pennapps.application",
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="applicant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="applications",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="first_hackathon",
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]
