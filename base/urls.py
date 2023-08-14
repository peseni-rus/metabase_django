from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'objecttypes', ObjectTypesViewSet)
# router.register(r'parametertypes', ParameterTypesViewSet)
router.register(r'parameters', ParametersViewSet,  basename='base')
# router.register(r'permissionobject', PermissionObjectViewSet)
router.register(r'objects', ObjectsViewSet, basename='base')
router.register(r'data', DataViewSet, basename='base')

urlpatterns = [
    path('', include(router.urls)),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
