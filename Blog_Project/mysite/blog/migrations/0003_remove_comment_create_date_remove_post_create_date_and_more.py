# Generated by Django 4.1.4 on 2023-07-06 17:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_text_alter_comment_create_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="create_date",
        ),
        migrations.RemoveField(
            model_name="post",
            name="create_date",
        ),
        migrations.AddField(
            model_name="comment",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 7, 6, 17, 30, 57, 274861, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 7, 6, 17, 30, 57, 273863, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
