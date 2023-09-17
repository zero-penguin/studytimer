# Generated by Django 3.2.20 on 2023-09-17 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_slide_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(upload_to='menber_face'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='contact_image'),
        ),
    ]
