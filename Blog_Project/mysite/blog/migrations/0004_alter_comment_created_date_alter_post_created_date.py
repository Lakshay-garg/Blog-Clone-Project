# Generated by Django 4.1.4 on 2023-07-07 02:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_remove_comment_create_date_remove_post_create_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 7, 7, 2, 56, 17, 969618, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 7, 7, 2, 56, 17, 968700, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
