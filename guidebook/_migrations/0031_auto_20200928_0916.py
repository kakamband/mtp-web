# Generated by Django 3.0.3 on 2020-09-28 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_setting', '0001_initial'),
        ('guidebook', '0030_remove_guidebook_cover_test_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guidebook',
            name='tag',
            field=models.ManyToManyField(to='sys_setting.Tag'),
        ),
    ]