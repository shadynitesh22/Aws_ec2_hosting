# Generated by Django 4.1.3 on 2022-11-14 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("author", models.CharField(max_length=200)),
                ("author_id", models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="randommodel",
            name="author",
            field=models.ForeignKey(
                default=2, on_delete=django.db.models.deletion.CASCADE, to="main.author"
            ),
        ),
    ]
