# Generated by Django 3.0.8 on 2020-07-19 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0032_auto_20200719_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='keyword',
            field=models.CharField(max_length=1000),
        ),
    ]
