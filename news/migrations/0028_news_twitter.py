# Generated by Django 3.0.8 on 2020-07-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0027_auto_20200715_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='twitter',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
