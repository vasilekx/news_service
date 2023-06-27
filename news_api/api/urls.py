# api/urls.py

from django.urls import include, path
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from .views import NewsViewSet, CommentViewSet


app_name = 'api'


router_v1 = routers.DefaultRouter()
router_v1.register(r'news', NewsViewSet, basename='news')
router_v1.register(
    r'news/(?P<news_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/auth/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
