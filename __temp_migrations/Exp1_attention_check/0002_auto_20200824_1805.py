# Generated by Django 2.2.4 on 2020-08-24 10:05

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Exp1_attention_check', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='Ans_one',
            field=otree.db.models.BooleanField(choices=[[False, 'Jakarta'], [False, 'Kucing'], [True, 'Joko Widodo'], [False, 'MaynilaMahathir bin Mohamad']], null=True, verbose_name='請根據您聽到的問題，選出最適合的答案'),
        ),
        migrations.AlterField(
            model_name='player',
            name='Ans_three',
            field=otree.db.models.LongStringField(null=True, verbose_name='請用印尼文寫下您聽到的句子'),
        ),
        migrations.AlterField(
            model_name='player',
            name='Ans_two',
            field=otree.db.models.BooleanField(choices=[[False, 'Joko Widodo'], [False, 'Mahathir bin Mohamad'], [True, 'Jakarta'], [False, 'Surabaya']], null=True, verbose_name='請根據您聽到的問題，選出最適合的答案'),
        ),
    ]
