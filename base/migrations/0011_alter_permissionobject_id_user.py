# Generated by Django 4.1 on 2022-08-22 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0010_objects_permissionobject_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissionobject',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
