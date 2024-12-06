# Generated by Django 5.1.4 on 2024-12-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0002_member_joined_date_member_phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("adı", models.CharField(max_length=255)),
                ("soyadı", models.CharField(max_length=255)),
                ("yurt", models.CharField(max_length=255)),
                ("sınıf", models.IntegerField(null=True)),
                ("seviye", models.IntegerField(null=True)),
            ],
        ),
    ]
