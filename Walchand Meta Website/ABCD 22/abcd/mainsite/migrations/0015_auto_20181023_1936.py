# Generated by Django 2.1.1 on 2018-10-23 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0014_remove_about_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='static/media')),
            ],
        ),
        migrations.RemoveField(
            model_name='home',
            name='image',
        ),
        migrations.RemoveField(
            model_name='home',
            name='mar2',
        ),
    ]
