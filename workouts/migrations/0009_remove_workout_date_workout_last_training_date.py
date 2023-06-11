# Generated by Django 4.1.7 on 2023-05-29 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0008_alter_exercises_muscle_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='date',
        ),
        migrations.AddField(
            model_name='workout',
            name='last_training_date',
            field=models.DateTimeField(null=True),
        ),
    ]