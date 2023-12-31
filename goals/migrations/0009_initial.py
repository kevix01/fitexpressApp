# Generated by Django 4.1.7 on 2023-05-30 14:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0008_delete_goals'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_type', models.TextField(choices=[('LOSE WEIGHT', 'LOSE WEIGHT'), ('MUSCLE STRENGTH', 'MUSCLE STRENGTH'), ('MUSCLE MASS', 'MUSCLE MASS'), ('BODY DEFINITION', 'BODY DEFINITION'), ('CARDIO', 'CARDIO')])),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('creation_date', models.DateField(default=datetime.datetime(2023, 5, 30, 14, 26, 4, 228214, tzinfo=datetime.timezone.utc))),
                ('estimated_finish_date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
