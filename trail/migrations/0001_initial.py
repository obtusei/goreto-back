# Generated by Django 5.1.1 on 2024-09-07 02:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('point_name', models.CharField(blank=True, choices=[('Starting', 'Starting'), ('End', 'End'), ('CheckPoint', 'CheckPoint')], max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='facts/')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.CharField(max_length=20)),
                ('length', models.FloatField()),
                ('duration', models.CharField(max_length=50)),
                ('temperature', models.CharField(blank=True, max_length=50, null=True)),
                ('safety_info', models.TextField(blank=True, null=True)),
                ('accessibility', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TravelMode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('Walking', 'Walking'), ('Cycling', 'Cycling')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('travel_mode', models.CharField(choices=[('Walking', 'Walking'), ('Cycling', 'Cycling')], max_length=20)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trail.property')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location_name', models.CharField(blank=True, max_length=255, null=True)),
                ('coordinates', models.ManyToManyField(blank=True, to='trail.coordinate')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('facts', models.ManyToManyField(blank=True, to='trail.fact')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trail.property')),
                ('review', models.ManyToManyField(blank=True, to='trail.review')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='places/')),
                ('facts', models.ManyToManyField(blank=True, to='trail.fact')),
                ('trails', models.ManyToManyField(blank=True, to='trail.trail')),
            ],
        ),
        migrations.CreateModel(
            name='TrailImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='trails/')),
                ('trail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='trail.trail')),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='mode',
            field=models.ManyToManyField(blank=True, to='trail.travelmode'),
        ),
    ]
