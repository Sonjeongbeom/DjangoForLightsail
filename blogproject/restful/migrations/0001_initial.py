# Generated by Django 3.2 on 2022-06-26 06:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('postDate', models.DateTimeField(default=datetime.datetime.now)),
                ('content', models.TextField()),
            ],
        ),
    ]
