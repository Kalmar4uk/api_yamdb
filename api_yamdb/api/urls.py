from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (APIGetToken, APISignup, CategoryViewSet, GengreViewSet,
                    ReviewViewSet, TitleViewSet, UsersViewSet)

router_v1 = DefaultRouter()
router_v1.register(r'api/v1/titles', TitleViewSet)
router_v1.register(r'api/v1/categories', CategoryViewSet)
router_v1.register(r'api/v1/genres', GengreViewSet)
router_v1.register(
    r'api/v1/titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    'users',
    UsersViewSet,
    basename='users'
)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/auth/token/', APIGetToken.as_view(), name='get_token'),
    path('v1/auth/signup/', APISignup.as_view(), name='signup'),
]
