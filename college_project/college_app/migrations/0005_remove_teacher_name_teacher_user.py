# Generated by Django 4.1.1 on 2022-10-25 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('college_app', '0004_rename_age_student_std_age_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='name',
        ),
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]