# Generated by Django 2.2.7 on 2019-12-18 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_tutorialcategory_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorialcategory',
            name='image',
        ),
    ]