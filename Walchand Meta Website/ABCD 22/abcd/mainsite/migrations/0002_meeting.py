# Generated by Django 2.1.1 on 2018-10-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('no', models.IntegerField(primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=32)),
                ('summary', models.CharField(max_length=2048)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
