# Generated by Django 3.0.5 on 2020-05-19 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='youtube',
            old_name='recommand',
            new_name='recommend',
        ),
    ]
