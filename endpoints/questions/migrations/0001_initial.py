# Generated by Django 2.1.1 on 2018-09-23 07:44

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseid', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=100)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
