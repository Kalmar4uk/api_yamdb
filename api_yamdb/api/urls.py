from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GengreViewSet, TitleViewSet, ReviewViewSet

router_v1 = DefaultRouter()
router_v1.register(r'api/v1/titles', TitleViewSet)
router_v1.register(r'api/v1/categories', CategoryViewSet)
router_v1.register(r'api/v1/genres', GengreViewSet)
router_v1.register(r'api/v1/titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews')

urlpatterns = [
    path('', include(router_v1.urls))
]
