# Generated by Django 3.2.20 on 2023-09-16 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_save'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='save',
            field=models.CharField(choices=[('not save', 'not save'), ('save', 'save')], max_length=10),
        ),
    ]
