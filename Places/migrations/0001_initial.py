# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 17:31
from __future__ import unicode_literals

import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placename', models.CharField(max_length=100, null=True)),
                ('placetype',
                 models.IntegerField(choices=[(0, 'Commercial'), (1, 'Private'), (2, 'Public')], default=0)),
                ('WiFiSSID', models.CharField(max_length=32, null=True)),
                ('WiFiPassword', models.CharField(max_length=32, null=True)),
                ('power',
                 models.IntegerField(choices=[(0, 'None'), (1, 'Limited'), (2, 'Good'), (3, 'Plenty')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Noiselevel', models.IntegerField(choices=[(0, 'Louder'), (1, 'Average'), (2, 'Quiet')], null=True)),
                ('Protips', models.CharField(max_length=1000, null=True)),
                ('OpenHour', models.TimeField(null=True)),
                ('CloseHour', models.TimeField(null=True)),
                ('Amenties', multiselectfield.db.fields.MultiSelectField(
                    choices=[('1', 'LoungeSeating'), ('2', 'Desk'), ('3', 'CommunityTables'), ('4', 'GroupFriendly'),
                             ('5', 'AirConditioner'), ('6', 'OutDoorSeating'), ('7', 'Pos'), ('8', 'NaturalLighting'),
                             ('9', 'HasFood'), ('10', 'Coffee'), ('11', 'EspressoDrink'), ('12', 'Tea'),
                             ('13', 'JuiceBar'), ('14', 'KidFriendly'), ('15', 'CarParking'), ('16', 'BikeParking')],
                    max_length=38, null=True)),
            ],
        ),
    ]
