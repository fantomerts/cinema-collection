# Generated by Django 3.2.7 on 2021-09-13 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20210913_1429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='actor_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='country_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='director',
            old_name='director_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='genre_name',
            new_name='name',
        ),
    ]
