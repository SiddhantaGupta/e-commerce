# Generated by Django 3.2.5 on 2021-08-22 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='phone_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='postal_code',
            field=models.IntegerField(),
        ),
    ]
