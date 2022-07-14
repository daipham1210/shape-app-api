from django.db.models import F
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from shape.models import Triangle, Rectangle, Diamond
from shape import serializers


class BaseShapeAttrViewSet(viewsets.ModelViewSet):
    """Base viewset for user owned recipe attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(
            user=self.request.user
        ).order_by('-name').distinct()

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)


class TriangleViewSet(BaseShapeAttrViewSet):
    queryset = Triangle.objects.all()
    serializer_class = serializers.TriangleSerializer


class RectangleViewSet(BaseShapeAttrViewSet):
    queryset = Rectangle.objects.all()
    serializer_class = serializers.RectangleSerializer

    def get_queryset(self):
        """Get list squares by params is_square"""
        is_square = bool(int(self.request.query_params.get('is_square', 0)))
        queryset = super().get_queryset()
        if is_square:
            queryset = queryset.filter(length=F('width'))
        return queryset


class DiamondViewSet(BaseShapeAttrViewSet):
    queryset = Diamond.objects.all()
    serializer_class = serializers.DiamondSerializer
