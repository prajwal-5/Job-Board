# Generated by Django 4.1.1 on 2022-09-16 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_job_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='mobile',
            field=models.CharField(max_length=12),
        ),
    ]
