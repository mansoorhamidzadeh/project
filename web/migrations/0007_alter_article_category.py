# Generated by Django 3.2 on 2023-04-02 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_remove_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='web.ArticleCategory'),
        ),
    ]
