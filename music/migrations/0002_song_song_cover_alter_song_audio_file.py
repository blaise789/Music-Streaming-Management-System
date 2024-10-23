# Generated by Django 5.1.2 on 2024-10-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_cover',
            field=models.ImageField(blank=True, upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(upload_to='media/songs'),
        ),
    ]