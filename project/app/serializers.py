from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist, ValidationError

from .models import *


class AreaSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=50)

    def create(self, data):
        return Area.objects.create(**data)


class CuratorSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=50)
    area_id = serializers.CharField(max_length=50)

    def create(self, data):
        AreaInstance = Area.objects.get(pk=data['area_id'])
        return Curator.objects.create(name=data['name'], area=AreaInstance)


class DisciplineSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=50)
    area_id = serializers.CharField(max_length=50)

    def create(self, data):
        AreaInstance = Area.objects.get(pk=data['area_id'])
        return Discipline.objects.create(title=data['title'], area=AreaInstance)


class GroupSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=50)
    area_id = serializers.CharField(max_length=50)

    def create(self, data):
        AreaInstance = Area.objects.get(pk=data['area_id'])
        return Group.objects.create(title=data['title'], area=AreaInstance)


class StudentSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=50)
    sex = serializers.CharField(max_length=50)
    group_id = serializers.CharField(max_length=50)

    def create(self, data):
        GroupInstance = Group.objects.get(pk=data['group_id'])
        return Student.objects.create(name=data['name'],sex=data['sex'], group=GroupInstance)
