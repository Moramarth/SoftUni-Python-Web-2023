# Generated by Django 4.2.2 on 2023-06-16 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_plant_belongs_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='plant_type',
            field=models.CharField(choices=[('Outdoor Plants', 'Outdoor Plants'), ('Indoor Plants', 'Indoor Plants')], max_length=14),
        ),
    ]