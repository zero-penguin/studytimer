# Generated by Django 4.2.2 on 2023-09-26 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_katakana'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='studyday_type',
            field=models.CharField(choices=[('a', '火曜１７時'), ('b', '火曜１８時'), ('c', '水曜１７時'), ('d', '水曜１８時'), ('e', '金曜１７時'), ('f', '金曜１８時'), ('g', '土曜１０時'), ('h', '土曜１１時'), ('i', '土曜１３時'), ('j', '土曜１４時')], max_length=10),
        ),
    ]
