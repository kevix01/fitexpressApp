# Generated by Django 4.1.7 on 2023-05-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birth',
            field=models.DateField(default='2001-07-25'),
            preserve_default=False,
        ),
    ]
