# Generated by Django 3.2 on 2021-04-30 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('article', '0003_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='articleLike', to='profiles.Profile'),
        ),
    ]
