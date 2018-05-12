# -*- encoding: utf-8 -*-
from django.shortcuts import render
from .models import AuthUser
from .serializers import AuthUserSerializer, ContentTypeSerializer, PermissionSerializer, GroupSerializer

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from rest_framework import viewsets


# Create your views here.
class AuthUserModelViewSet(viewsets.ModelViewSet):
    model            = AuthUser
    serializer_class = AuthUserSerializer
    queryset         = AuthUser.objects.all()
    queryset_detail  = queryset.prefetch_related('groups__permissions')


class PermissionModelViewSet(viewsets.ModelViewSet):
    model            = Permission
    serializer_class = PermissionSerializer
    queryset         = Permission.objects.all()


class GroupModelViewSet(viewsets.ModelViewSet):
    model            = Group
    serializer_class = GroupSerializer
    queryset         = Group.objects.all()


class ContentTypeModelViewSet(viewsets.ModelViewSet):
    model            = ContentType
    serializer_class = ContentTypeSerializer
    queryset         = ContentType.objects.all()