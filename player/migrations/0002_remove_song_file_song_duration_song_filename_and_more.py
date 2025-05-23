# Generated by Django 5.2 on 2025-05-05 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='file',
        ),
        migrations.AddField(
            model_name='song',
            name='duration',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='song',
            name='filename',
            field=models.CharField(default='default_filename.mp3', max_length=255),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
