# Generated by Django 4.1.7 on 2023-06-02 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0018_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goals',
            name='complete_date',
            field=models.DateField(null=True),
        ),
    ]
