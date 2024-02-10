from django.urls import include, path
from rest_framework import routers

from api.views import (APISignup, APIToken, CategoryViewSet, CommentViewSet,
                       GengreViewSet, ReviewViewSet, TitleViewSet,
                       UsersViewSet)

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(
    'categories',
    CategoryViewSet,
    basename='categories'
)
router_v1.register(
    'genres',
    GengreViewSet,
    basename='genres'
)
router_v1.register(
    'titles',
    TitleViewSet,
    basename='titles'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register(
    'users',
    UsersViewSet,
    basename='users'
)

auth_urls = [
    path('signup/', APISignup.as_view(), name='signup'),
    path('token/', APIToken.as_view(), name='token')
]

urlpatterns = [
    path('v1/auth/', include(auth_urls)),
    path('v1/', include(router_v1.urls))
]
