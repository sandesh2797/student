# Generated by Django 3.2.5 on 2021-08-13 10:31

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('highfitapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='myfit',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='myfit',
            name='phone_number',
            field=models.CharField(max_length=255),
        ),
    ]
