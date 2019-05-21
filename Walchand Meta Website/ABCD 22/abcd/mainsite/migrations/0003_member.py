# Generated by Django 2.1.1 on 2018-10-15 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_meeting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('post', models.CharField(max_length=32)),
                ('image', models.ImageField(upload_to='prof_image')),
                ('phn_number', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('info', models.TextField(max_length=200)),
                ('address', models.CharField(max_length=400)),
            ],
        ),
    ]
