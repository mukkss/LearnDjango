# Generated by Django 5.1.6 on 2025-02-23 14:20


# After creating models Run these two commands
# 1. python manage.py makemigration (will create an file to make tables in the MySQL)
# 2. python manage.py migrate (will create the tables in the MySQL)
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="img_url",
            field=models.URLField(null=True),
        ),
    ]
