# Generated by Django 2.2.7 on 2019-11-07 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20191107_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorialcategory',
            name='image',
        ),
    ]