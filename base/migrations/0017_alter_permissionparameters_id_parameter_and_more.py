# Generated by Django 4.1 on 2022-08-29 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0016_objects_object_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissionparameters',
            name='id_parameter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.parameters'),
        ),
        migrations.AlterField(
            model_name='permissionparameters',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
