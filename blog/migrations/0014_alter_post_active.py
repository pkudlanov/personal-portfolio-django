# Generated by Django 3.2.7 on 2022-04-04 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20220404_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
