# Generated by Django 3.0.3 on 2020-10-13 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_liked_email',
            field=models.BooleanField(default=True),
        ),
    ]
