# Generated by Django 3.0.2 on 2020-01-26 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(default='DEFAULT DESCRIPTION', max_length=255),
        ),
    ]