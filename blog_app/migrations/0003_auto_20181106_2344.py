# Generated by Django 2.1.3 on 2018-11-07 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_theme'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Theme',
        ),
        migrations.AddField(
            model_name='post',
            name='intro',
            field=models.CharField(default=None, max_length=500),
        ),
    ]
