from rest_framework import serializers
from .models import BaseShapeModel, Triangle, Rectangle, Diamond
from django.db.models import F


class BaseShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseShapeModel
        fields = ('id', 'name', 'area', 'perimeter')
        abstract = True
        read_only_fields = ('id',)


class TriangleSerializer(BaseShapeSerializer):
    class Meta:
        model = Triangle
        fields = BaseShapeSerializer.Meta.fields + ('side1', 'side2', 'side3')


class RectangleSerializer(BaseShapeSerializer):
    class Meta:
        model = Rectangle
        fields = BaseShapeSerializer.Meta.fields + ('length', 'width')


class DiamondSerializer(BaseShapeSerializer):
    class Meta:
        model = Diamond
        fields = BaseShapeSerializer.Meta.fields + ('diagonal1', 'diagonal2', 'side')
