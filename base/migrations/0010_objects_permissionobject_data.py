# Generated by Django 4.1 on 2022-08-22 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_permissionobject_id_object_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objects',
            fields=[
                ('id_object', models.AutoField(primary_key=True, serialize=False)),
                ('id_object_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.objecttypes')),
            ],
        ),
        migrations.CreateModel(
            name='PermissionObject',
            fields=[
                ('id_permission_object', models.AutoField(primary_key=True, serialize=False)),
                ('read', models.BooleanField()),
                ('create', models.BooleanField()),
                ('id_object', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.objects')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.users')),
            ],
            options={
                'ordering': ['id_permission_object'],
            },
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id_record', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(help_text='Record date time.')),
                ('value', models.CharField(help_text='Value record', max_length=10)),
                ('id_object', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.objects')),
                ('id_parameter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.parameters')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.users')),
            ],
            options={
                'ordering': ['datetime'],
            },
        ),
    ]