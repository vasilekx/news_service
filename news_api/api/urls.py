# api/urls.py

from django.urls import include, path
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

# from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


app_name = 'api'

# router_v1 = routers.DefaultRouter()
# router_v1.register(r'users', UserViewSet, basename='user')
# router_v1.register(r'posts', PostViewSet, basename='posts')
# router_v1.register(r'groups', GroupViewSet, basename='groups')
# router_v1.register(
#     r'posts/(?P<post_id>\d+)/comments',
#     CommentViewSet,
#     basename='comment'
# )
# router_v1.register(r'follow', FollowViewSet, basename='follow')


# urlpatterns = [
#     path('v1/', include('djoser.urls.jwt')),
#     path('v1/', include(router_v1.urls)),
# ]

urlpatterns = [
    # path('v1/', include(router_v1.urls)),
    # path('v1/auth/', include(auth_urlpatterns)),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]