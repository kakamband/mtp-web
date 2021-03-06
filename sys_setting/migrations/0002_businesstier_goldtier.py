# Generated by Django 3.0.3 on 2020-10-27 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import storages.backends.s3boto3
import sys_setting.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sys_setting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessTier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('logo', models.ImageField(blank=True, null=True, storage=storages.backends.s3boto3.S3Boto3Storage(bucket=''), upload_to=sys_setting.models.image_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='GoldTier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
