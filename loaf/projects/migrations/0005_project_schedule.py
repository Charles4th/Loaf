# Generated by Django 2.0.7 on 2018-07-22 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_max_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='schedule',
            field=models.CharField(default=0, max_length=140),
        ),
    ]