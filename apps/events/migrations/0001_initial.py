# Generated by Django 3.1.2 on 2020-10-23 01:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, help_text='a detailed description of the event', verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Stand',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stands', to='events.event', verbose_name='Event')),
            ],
            options={
                'verbose_name': 'Stand',
                'verbose_name_plural': 'Stands',
                'ordering': ['event__name', 'name'],
            },
        ),
    ]
