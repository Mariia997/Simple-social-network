# Generated by Django 3.1 on 2020-08-30 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200830_1444'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='UserPost',
        ),
    ]
