# Generated by Django 3.2.9 on 2021-11-23 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentmodel',
            options={'ordering': ['-date_created']},
        ),
        migrations.RemoveField(
            model_name='commentmodel',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='commentmodel',
            name='time_created',
        ),
        migrations.RemoveField(
            model_name='commentmodel',
            name='time_updated',
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
