from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken import views

from .views import (CategoryApiView,
                    AuthorApiView,
                    OrganizationApiView,
                    TagApiView,
                    PostApiView
                    )

router = routers.DefaultRouter()
router.register('categories', CategoryApiView)
router.register('authors', AuthorApiView)
router.register('organizations', OrganizationApiView)
router.register('tags', TagApiView)
router.register('posts', PostApiView)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    # path('api-token-auth/', views.obtain_auth_token),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]
