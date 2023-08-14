from django.contrib import admin
from .models import *


class ParametersAdmin(admin.ModelAdmin):
    list_display = ['parameter', 'id_parameter_type', 'id_object_type', 'id_parameter',]
    list_filter = ['id_parameter_type', 'id_object_type', ]


class ObjectsAdmin(admin.ModelAdmin):
    list_display = ['object_description', 'id_object_type', 'id_object', ]
    list_filter = ['id_object_type', 'object_description']


class ParameterTypesAdmin(admin.ModelAdmin):
    list_display = ['parameter_type', 'description_parameter_type', ]


class ObjectTypesAdmin(admin.ModelAdmin):
    list_display = ['object_type', 'description_object_type']


class DataAdmin(admin.ModelAdmin):
    list_display = ['datetime_record', 'id_object', 'id_parameter', 'value', 'id_user', ]
    list_filter = ['id_object', 'id_parameter', 'id_user', ]


class PermissionObjectAdmin(admin.ModelAdmin):
    list_display = ['id_user', 'id_object', 'read', 'create']
    list_filter = ['id_user', 'id_object']


class PermissionParametersAdmin(admin.ModelAdmin):
    list_display = ['id_user', 'id_parameter', 'read', 'create']
    list_filter = ['id_user',  'id_parameter']


admin.site.register(PermissionParameters, PermissionParametersAdmin)
admin.site.register(PermissionObject, PermissionObjectAdmin)
admin.site.register(Parameters, ParametersAdmin)
admin.site.register(Objects, ObjectsAdmin)
admin.site.register(ParameterTypes, ParameterTypesAdmin)
admin.site.register(ObjectTypes, ObjectTypesAdmin)
admin.site.register(Data, DataAdmin)



