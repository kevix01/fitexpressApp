# Generated by Django 4.1.7 on 2023-05-30 14:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0006_alter_goals_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goals',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 30, 14, 21, 4, 481756, tzinfo=datetime.timezone.utc)),
        ),
    ]
