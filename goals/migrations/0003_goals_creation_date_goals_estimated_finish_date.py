# Generated by Django 4.1.7 on 2023-05-30 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_remove_goals_kcal_rep_goals_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='goals',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, default='10/06/2023'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goals',
            name='estimated_finish_date',
            field=models.DateTimeField(default='10-06-2023'),
            preserve_default=False,
        ),
    ]
