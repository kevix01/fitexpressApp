# Generated by Django 4.1.7 on 2023-06-07 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_customuser_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birth',
            field=models.DateField(null=True),
        ),
    ]
