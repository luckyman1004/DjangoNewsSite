# Generated by Django 3.0.8 on 2020-07-12 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='top_trending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='trending_today',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='news',
            old_name='image1',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='slider',
            old_name='image1',
            new_name='image_size_950x280',
        ),
        migrations.RemoveField(
            model_name='news',
            name='slider',
        ),
        migrations.RemoveField(
            model_name='news',
            name='trending',
        ),
    ]