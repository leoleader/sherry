# Generated by Django 4.1.5 on 2023-01-30 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0010_alter_quizmodel_cover"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quizmodel",
            name="cover",
            field=models.ImageField(
                blank=True, default="quiz-photo.jpeg", null=True, upload_to="images/"
            ),
        ),
    ]
