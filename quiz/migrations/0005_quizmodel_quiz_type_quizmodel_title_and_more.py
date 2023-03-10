# Generated by Django 4.1.5 on 2023-01-26 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0004_alter_quesmodel_quiz"),
    ]

    operations = [
        migrations.AddField(
            model_name="quizmodel",
            name="quiz_type",
            field=models.CharField(
                choices=[("knowledge", "Knowledge"), ("personality", "Personality")],
                default="knowledge",
                max_length=15,
            ),
        ),
        migrations.AddField(
            model_name="quizmodel",
            name="title",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="quizmodel",
            name="blurb",
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.CreateModel(
            name="Personality",
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
                ("title", models.CharField(max_length=200, null=True)),
                ("blurb", models.CharField(max_length=600, null=True)),
                (
                    "quiz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="quiz.quizmodel"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PersModel",
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
                ("question", models.CharField(max_length=200, null=True)),
                ("op1", models.CharField(max_length=200, null=True)),
                ("op2", models.CharField(max_length=200, null=True)),
                ("op3", models.CharField(max_length=200, null=True)),
                ("op4", models.CharField(max_length=200, null=True)),
                (
                    "ans1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ans1",
                        to="quiz.personality",
                    ),
                ),
                (
                    "ans2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ans2",
                        to="quiz.personality",
                    ),
                ),
                (
                    "ans3",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ans3",
                        to="quiz.personality",
                    ),
                ),
                (
                    "ans4",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ans4",
                        to="quiz.personality",
                    ),
                ),
                (
                    "quiz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="quiz.quizmodel"
                    ),
                ),
            ],
        ),
    ]
