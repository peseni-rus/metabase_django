from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime


class ParameterTypes(models.Model):
    """Description of the parameter type."""
    id_parameter_type = models.AutoField(primary_key=True)
    parameter_type = models.CharField(
        max_length=10,
        help_text="Type name."
    )
    description_parameter_type = models.CharField(
        max_length=50,
        help_text="Type name description."
    )

    def __str__(self):
        return str(self.parameter_type) + ' / ' + str(self.id_parameter_type)

    class Meta:
        ordering = ['parameter_type', ]


class ObjectTypes(models.Model):
    """Description of the object type."""
    id_object_type = models.AutoField(primary_key=True)
    object_type = models.CharField(
        max_length=20,
        help_text="Object type name."
    )
    description_object_type = models.CharField(
        max_length=50,
        help_text="Object type description."
    )

    def __str__(self):
        return str(self.object_type) + ' / ' + str(self.id_object_type)

    class Meta:
        ordering = ['object_type', ]


class Parameters(models.Model):
    """Description of the parameter."""
    id_parameter = models.AutoField(primary_key=True)

    id_parameter_type = models.ForeignKey(ParameterTypes, on_delete=models.PROTECT)

    id_object_type = models.ForeignKey(ObjectTypes, on_delete=models.PROTECT)

    parameter = models.CharField(
        max_length=200,
        help_text="Parameter name."
    )
    measure_unit = models.CharField(
        max_length=50,
        help_text="Object type description."
    )
    default_value = models.CharField(
        max_length=200,
        help_text="Default value",
        default='',
        blank=True
    )

    def __str__(self):
        return str(self.parameter) + ' / ' + str(self.id_object_type)

    class Meta:
        ordering = ['id_parameter', ]


class Objects(models.Model):
    id_object = models.AutoField(primary_key=True)
    id_object_type = models.ForeignKey(ObjectTypes, on_delete=models.CASCADE, db_index=True)
    object_description = models.CharField(
        max_length=200,
        help_text="Description",
        default='-',
        unique=True
    )

    def __str__(self):
        return str(self.id_object) + ' / ' + str(self.object_description)


class Data(models.Model):
    """Main storage"""
    id_record = models.AutoField(primary_key=True)

    id_object = models.ForeignKey(Objects, on_delete=models.PROTECT)

    id_parameter = models.ForeignKey(Parameters, on_delete=models.PROTECT)

    datetime_record = models.DateTimeField(
        help_text="Date and time of record.",
        auto_now_add=True
    )
    datetime_data = models.DateTimeField(
        help_text="Date and time of data.",
        default=datetime.now,
        blank=True
    )
    value = models.CharField(
        max_length=200,
        help_text="Value record"
    )

    id_user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id_record)

    def get_absolute_url(self):
        return reverse('records', args=[str(self.id_record)])

    class Meta:
        ordering = ['datetime_record', ]


class PermissionParameters(models.Model):
    """Main storage"""
    id_permission_parameter = models.AutoField(primary_key=True)

    id_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    id_parameter = models.ForeignKey(Parameters, on_delete=models.DO_NOTHING)

    read = models.BooleanField()
    create = models.BooleanField()

    def __str__(self):
        return str(self.id_permission_parameter)

    class Meta:
        ordering = ['id_permission_parameter', ]


class PermissionObject(models.Model):
    """Main storage"""
    id_permission_object = models.AutoField(primary_key=True)

    id_user = models.ForeignKey(User, on_delete=models.PROTECT)

    id_object = models.ForeignKey(Objects, on_delete=models.PROTECT)

    read = models.BooleanField()
    create = models.BooleanField()

    def __str__(self):
        return str(self.id_object)

    class Meta:
        ordering = ['id_permission_object', ]

