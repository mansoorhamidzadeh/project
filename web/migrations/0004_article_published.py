# Generated by Django 3.2 on 2023-03-29 16:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20230329_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
