from django.urls import include, path
from rest_framework import routers

from users.views import AdminViewSet, UserView
from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitlesViewSet)

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register(r'v1/titles', TitlesViewSet)
router_v1.register(r'v1/categories', CategoryViewSet)
router_v1.register(r'v1/genres', GenreViewSet)
router_v1.register(r'v1/users', AdminViewSet)
router_v1.register(
    r'v1/titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='review'
)
router_v1.register(
    r'v1/titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comment'
)

urlpatterns = [
    path('v1/users/me/', UserView.as_view()),
    path('', include(router_v1.urls))
]