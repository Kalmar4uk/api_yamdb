from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GengreViewSet, TitleViewSet

router_v1 = DefaultRouter()
router_v1.register(r'api/v1/titles', TitleViewSet)
router_v1.register(r'api/v1/categories', CategoryViewSet)
router_v1.register(r'api/v1/genres', GengreViewSet)

urlpatterns = [
    path('', include(router_v1.urls))
]
