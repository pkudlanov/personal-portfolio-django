# Generated by Django 3.2.7 on 2021-09-22 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20210811_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url_github',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, to='portfolio.Tag'),
        ),
    ]
