# Generated by Django 5.1.2 on 2024-10-24 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]