# Generated by Django 4.1.5 on 2023-01-26 21:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0008_rename_whislist_whishlist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Whishlist',
            new_name='Wishlist',
        ),
    ]
