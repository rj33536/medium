# Generated by Django 3.0.2 on 2020-03-24 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200324_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
