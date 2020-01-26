# Generated by Django 3.0.2 on 2020-01-25 18:57

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='DEFAULT ITEM', max_length=255)),
                ('description', models.CharField(default='DEFAULT DESCRIPTION', max_length=255)),
                ('value', models.IntegerField(default=0)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tileset', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), size=None)),
                ('map', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), size=None)),
                ('colors', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='DEFAULT TITLE', max_length=50)),
                ('description', models.CharField(default='DEFAULT DESCRIPTION', max_length=500)),
                ('n_to', models.IntegerField(default=0)),
                ('e_to', models.IntegerField(default=0)),
                ('s_to', models.IntegerField(default=0)),
                ('w_to', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Gem',
            fields=[
                ('items_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='piratestwo.Items')),
                ('rarity', models.CharField(default='', max_length=50)),
            ],
            bases=('piratestwo.items',),
        ),
        migrations.CreateModel(
            name='Gold',
            fields=[
                ('items_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='piratestwo.Items')),
            ],
            bases=('piratestwo.items',),
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('items_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='piratestwo.Items')),
                ('attack_power', models.IntegerField(default=0)),
                ('durability', models.IntegerField(default=100)),
            ],
            bases=('piratestwo.items',),
        ),
    ]