# Generated by Django 4.1.1 on 2022-10-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.IntegerField()),
                ('Name', models.CharField(max_length=225)),
                ('Course', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]