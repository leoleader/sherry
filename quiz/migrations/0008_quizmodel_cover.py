# Generated by Django 4.1.5 on 2023-01-30 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0007_alter_quizmodel_creator_alter_userprofile_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="quizmodel",
            name="cover",
            field=models.ImageField(null=True, upload_to="images/"),
        ),
    ]
