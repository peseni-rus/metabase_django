# Generated by Django 4.1 on 2022-09-05 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_permissionparameters_id_parameter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameters',
            name='measure_unit',
            field=models.CharField(help_text='Object type description.', max_length=50),
        ),
        migrations.AlterField(
            model_name='parameters',
            name='parameter',
            field=models.CharField(help_text='Parameter name.', max_length=100),
        ),
    ]
