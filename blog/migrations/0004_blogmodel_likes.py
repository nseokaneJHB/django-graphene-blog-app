# Generated by Django 3.2.9 on 2021-11-23 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blogmodel_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='likes',
            field=models.ManyToManyField(blank=True, to='blog.LikeModel'),
        ),
    ]