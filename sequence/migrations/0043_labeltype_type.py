# Generated by Django 3.0.3 on 2020-09-24 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0042_auto_20200924_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='labeltype',
            name='type',
            field=models.CharField(choices=[('point', 'point'), ('polygon', 'polygon')], default='point', max_length=50),
        ),
    ]
