from abc import ABC

from rest_framework import serializers

from .models import ObjectTypes, ParameterTypes, Parameters, Objects, Data, PermissionObject
from django.contrib.auth.models import User


class ObjectTypesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ObjectTypes
        fields = ('id_object_type', 'object_type', 'description_object_type')


class ParameterTypesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ParameterTypes
        fields = ('id_parameter_type', 'parameter_type', 'description_parameter_type')


class ParametersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Parameters
        fields = '__all__'


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ObjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Objects
        fields = '__all__'


class DataSerializers(serializers.ModelSerializer):
    id_user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Data
        fields = '__all__'


class PermissionObjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = PermissionObject
        fields = '__all__'
