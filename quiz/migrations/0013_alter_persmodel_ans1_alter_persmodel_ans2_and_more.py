# Generated by Django 4.1.5 on 2023-05-10 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0012_alter_quizmodel_cover"),
    ]

    operations = [
        migrations.AlterField(
            model_name="persmodel",
            name="ans1",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="persmodel",
            name="ans2",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="persmodel",
            name="ans3",
            field=models.CharField(blank=True, default="", max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="persmodel",
            name="ans4",
            field=models.CharField(blank=True, default="", max_length=200, null=True),
        ),
    ]
