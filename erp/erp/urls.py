#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

#from auth_users.views import AuthUserModelViewSet, PermissionModelViewSet, GroupModelViewSet, ContentTypeModelViewSet

router = routers.DefaultRouter()

#router.register(r'auth-users', AuthUserModelViewSet)
#router.register(r'permissions', PermissionModelViewSet)
#router.register(r'groups', GroupModelViewSet)
#router.register(r'content_type', ContentTypeModelViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #A.P.I - R.E.S.T.
    url(r'^api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
