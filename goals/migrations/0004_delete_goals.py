# Generated by Django 4.1.7 on 2023-05-30 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0003_goals_creation_date_goals_estimated_finish_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Goals',
        ),
    ]