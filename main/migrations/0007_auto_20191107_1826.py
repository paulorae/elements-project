# Generated by Django 2.2.7 on 2019-11-07 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20191107_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
