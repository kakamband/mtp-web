# Generated by Django 3.0.3 on 2020-09-29 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0005_sequenceweather'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequenceweather',
            name='current_observation_time',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sequenceweather',
            name='his_astro_moonrise',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sequenceweather',
            name='his_astro_moonset',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sequenceweather',
            name='his_astro_sunrise',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sequenceweather',
            name='his_astro_sunset',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
