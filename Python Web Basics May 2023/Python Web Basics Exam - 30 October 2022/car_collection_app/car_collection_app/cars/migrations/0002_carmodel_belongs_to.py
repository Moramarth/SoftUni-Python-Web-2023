# Generated by Django 4.2.2 on 2023-06-16 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profilemodel_age'),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='belongs_to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.profilemodel'),
            preserve_default=False,
        ),
    ]