# Generated by Django 3.2.20 on 2023-09-28 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20230928_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='katakana',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='account',
            name='school',
            field=models.CharField(max_length=20),
        ),
    ]
