# Generated by Django 4.0.6 on 2023-04-12 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_warmup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherrecipient',
            name='imap_host',
            field=models.CharField(default='', max_length=50),
        ),
    ]
