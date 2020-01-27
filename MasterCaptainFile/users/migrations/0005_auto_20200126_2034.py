# Generated by Django 3.0.2 on 2020-01-27 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200126_2024'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerItems',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('username', models.CharField(default='DEFAULT DESCRIPTION', max_length=255, unique=True)),
                ('gold', models.IntegerField(default=0)),
                ('gem', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]