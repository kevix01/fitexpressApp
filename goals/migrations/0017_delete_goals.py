# Generated by Django 4.1.7 on 2023-06-01 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0016_remove_goals_estimated finish date must be greater than or equal today!'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Goals',
        ),
    ]
