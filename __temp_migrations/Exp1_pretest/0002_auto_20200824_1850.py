# Generated by Django 2.2.4 on 2020-08-24 10:50

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Exp1_pretest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='decision_duration',
            field=otree.db.models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='num_listen_times',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
    ]
