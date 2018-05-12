# -*- encoding: utf-8 -*-
from django.contrib.auth.models import Group,Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from .models import AuthUser


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class ContentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Permission
		fields = '__all__'


class AuthUserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = AuthUser
		fields = '__all__'