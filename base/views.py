import os
import sys

from django.db.models.expressions import RawSQL
from django.http import FileResponse
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import ObjectTypesSerializers, ParameterTypesSerializers, \
    ParametersSerializers, UsersSerializers, ObjectsSerializers, DataSerializers, PermissionObjectsSerializers
from .models import ObjectTypes, ParameterTypes, Parameters, Objects, PermissionObject, Data
from django.contrib.auth.models import User


user_data = list(User.objects.filter(is_staff=1).values())
staff_users = []
for user in user_data:
    staff_users.append(user.get('id'))


def get_index(request):
    print(sys.path)

    return FileResponse(open(os.sep + 'base' + os.sep + 'static' + os.sep + 'index.html'))


class ModelReadCreateViewSet(mixins.CreateModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.ListModelMixin,
                             GenericViewSet):
    pass


class ParametersViewSet(ModelReadCreateViewSet):
    def get_queryset(self):
        current_user = self.request.user.id
        if current_user in staff_users:
            data = Parameters.objects.all().order_by('id_parameter')
            return data
        str_sql = 'SELECT DISTINCT base_parameters.id_parameter FROM base_parameters JOIN base_permissionparameters \
        ON base_parameters.id_parameter = base_permissionparameters.id_parameter_id \
        WHERE base_permissionparameters.id_user_id = %s AND base_permissionparameters."read" = 1'
        data = Parameters.objects.filter(id_parameter__in=RawSQL(str_sql, [current_user, ]))
        return data

    # queryset = Parameters.objects.all()
    serializer_class = ParametersSerializers
    permission_classes = (IsAuthenticated, )
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_parameter_type', 'id_object_type', 'parameter', 'measure_unit']


class ParameterTypesViewSet(ModelReadCreateViewSet):
    queryset = ParameterTypes.objects.all().order_by('id_parameter_type')
    serializer_class = ParameterTypesSerializers
    permission_classes = (IsAuthenticated, )
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["parameter_type", "description_parameter_type"]


class UsersViewSet(ModelReadCreateViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UsersSerializers
    permission_classes = (IsAdminUser, )


class DataViewSet(ModelReadCreateViewSet):

    def get_queryset(self):
        current_user = self.request.user.id
        if current_user in staff_users:
            data = Data.objects.all().order_by('-id_record')
            return data
        str_sql = 'SELECT DISTINCT\
        base_data.id_record \
        FROM ((base_data JOIN base_permissionobject ON base_data.id_object_id = base_permissionobject.id_object_id) \
        JOIN base_permissionparameters ON base_data.id_parameter_id = base_permissionparameters.id_parameter_id) \
        JOIN base_parameters ON base_parameters.id_parameter = base_data.id_parameter_id \
        WHERE base_permissionobject.id_user_id = %s and base_permissionparameters.id_user_id = %s AND \
        base_permissionobject."read"=1'
        data = Data.objects.filter(id_record__in=RawSQL(str_sql, [current_user, current_user])).order_by('-id_record')

        return data

    '''def create(self, request, *args, **kwargs):
        queryset = Data.objects.all()
        serializer = DataSerializers(queryset, many=True)
        serializer.data(request.data)
        
        # serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    # queryset = Data.objects.all()
    '''
    serializer_class = DataSerializers #(many=True)
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_object', 'id_parameter', 'datetime_record', 'datetime_data', 'value', 'id_user']


class ObjectTypesViewSet(ModelReadCreateViewSet):
    queryset = ObjectTypes.objects.all().order_by('id_object_type')
    serializer_class = ObjectTypesSerializers
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []


class PermissionObjectViewSet(ModelReadCreateViewSet):
    queryset = PermissionObject.objects.all().order_by('id_permission_object')
    serializer_class = PermissionObjectsSerializers
    permission_classes = (IsAdminUser,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_user', 'id_object',]


class ObjectsViewSet(ModelReadCreateViewSet):

    def get_queryset(self):
        current_user = self.request.user.id
        if current_user in staff_users:
            data = Objects.objects.all().order_by('-id_object')
            return data
        str_sql = 'SELECT DISTINCT base_objects.id_object \
        FROM base_objects JOIN base_permissionobject ON base_objects.id_object = base_permissionobject.id_object_id \
        WHERE base_permissionobject.id_user_id = %s AND  base_permissionobject."read"=1'
        data = Objects.objects.filter(id_object__in=RawSQL(str_sql, [current_user, ])).order_by('-id_object')
        return data

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        a_record = PermissionObject(id_user_id=self.request.user.id,
                                    id_object_id=serializer.data['id_object'],
                                    read=True,
                                    create=True)
        a_record.save()

        '''user_data = list(User.objects.filter(is_staff=1).values())
        for user in user_data:
            a_record = PermissionObject(id_user_id=user.get('id'),
                                        id_object_id=serializer.data['id_object'],
                                        read=True,
                                        create=True)
            a_record.save()'''
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # queryset = Data.objects.all()

    serializer_class = ObjectsSerializers
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_object', 'id_object_type', 'object_description', ]
