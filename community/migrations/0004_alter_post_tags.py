# Generated by Django 3.2.19 on 2023-06-27 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20230627_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='community.Tag'),
        ),
    ]
