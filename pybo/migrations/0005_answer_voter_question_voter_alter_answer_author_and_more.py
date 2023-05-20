# Generated by Django 4.2.1 on 2023-05-20 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pybo", "0004_answer_modify_date_question_modify_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="voter",
            field=models.ManyToManyField(
                related_name="voter_answer", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="voter",
            field=models.ManyToManyField(
                related_name="voter_question", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="answer",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="author_answer",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="question",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="author_question",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
