# Generated by Django 3.2 on 2021-05-08 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_alter_comments_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.CharField(max_length=1000),
        ),
    ]
