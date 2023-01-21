# Generated by Django 4.1.5 on 2023-01-21 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='address',
            new_name='locality',
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.IntegerField(default=3706),
        ),
    ]
