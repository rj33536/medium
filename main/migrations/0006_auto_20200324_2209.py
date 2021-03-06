# Generated by Django 3.0.2 on 2020-03-24 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_auto_20200324_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='claps',
            field=models.ManyToManyField(related_name='clappers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='clap',
        ),
    ]
