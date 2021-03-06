# Generated by Django 3.0.2 on 2020-01-24 03:28

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
            name='Weapon',
            fields=[
                ('items_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pirateAdventure.Items')),
                ('attack_power', models.IntegerField(default=0)),
                ('durability', models.IntegerField(default=100)),
            ],
            bases=('pirateAdventure.items',),
        ),
    ]
