# Generated by Django 2.0.7 on 2020-10-12 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planName', models.CharField(max_length=100)),
                ('typeName', models.CharField(max_length=50)),
            ],
        ),
    ]
