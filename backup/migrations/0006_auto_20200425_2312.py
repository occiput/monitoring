# Generated by Django 3.0.4 on 2020-04-25 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0005_auto_20200425_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balls',
            name='dick',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='specialists.Specialist'),
        ),
    ]
