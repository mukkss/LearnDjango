# Generated by Django 5.1.6 on 2025-03-06 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_post_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slugs",
            field=models.SlugField(blank=True, null=True),
        ),
    ]
