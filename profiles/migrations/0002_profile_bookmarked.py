# Generated by Django 3.2 on 2021-05-04 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_delete_savearticle'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bookmarked',
            field=models.ManyToManyField(to='article.Article'),
        ),
    ]
