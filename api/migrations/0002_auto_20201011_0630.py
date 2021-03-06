# Generated by Django 3.1.1 on 2020-10-11 06:30

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='contactEmail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='formLink',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=200)),
                ('fromtimestamp', models.DateTimeField()),
                ('totimestamp', models.DateTimeField()),
                ('desc', models.TextField()),
                ('image', models.FileField(blank=True, null=True, upload_to=api.models.uploadTimelineImg)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeline', to='api.event')),
            ],
            options={
                'verbose_name': 'Timeline',
                'verbose_name_plural': 'Timelines',
                'db_table': 'timeline',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=200)),
                ('userNumber', models.CharField(max_length=13)),
                ('userEmail', models.EmailField(blank=True, max_length=254, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allRegistrations', to='api.event')),
            ],
            options={
                'verbose_name': 'Registration',
                'verbose_name_plural': 'Registrations',
                'db_table': 'registration',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(default=-1)),
                ('rankRange', models.CharField(max_length=8)),
                ('desc', models.TextField()),
                ('img', models.FileField(blank=True, null=True, upload_to=api.models.uploadPrizeImg)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prizes', to='api.event')),
            ],
            options={
                'verbose_name': 'Prize',
                'verbose_name_plural': 'Prizes',
                'db_table': 'prize',
                'managed': True,
            },
        ),
    ]
