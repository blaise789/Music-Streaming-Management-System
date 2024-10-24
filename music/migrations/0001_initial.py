# Generated by Django 5.1.2 on 2024-10-24 08:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('duration', models.DurationField()),
                ('audio_file', models.FileField(upload_to='media/songs')),
                ('song_cover', models.ImageField(blank=True, upload_to='media/images')),
                ('genre', models.CharField(choices=[('Pop', 'Pop'), ('Rock', 'Rock'), ('Hip-hop', 'Hip-hop')], max_length=50)),
                ('release_year', models.PositiveIntegerField(blank=True, null=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='albums.album')),
            ],
            options={
                'db_table': 'songs',
            },
        ),
    ]
