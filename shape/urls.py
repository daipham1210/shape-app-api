from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shape import views

router = DefaultRouter()
router.register('triangles', views.TriangleViewSet)
router.register('rectangles', views.RectangleViewSet)
router.register('diamonds', views.DiamondViewSet)
app_name = 'shape'

urlpatterns = [
    path('', include(router.urls))
]
  