# Generated by Django 4.1.1 on 2022-10-18 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('img_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentregistration',
            old_name='photo',
            new_name='image',
        ),
    ]