# Generated by Django 3.0.2 on 2020-03-29 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200329_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile'),
        ),
    ]
