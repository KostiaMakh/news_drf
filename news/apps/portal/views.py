from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken

from .models import (Author,
                     Category,
                     Organization,
                     Tag,
                     Post,
                     )

from .serializers import (AuthorSerializer,
                          AuthorPostSerializer,
                          CategorySerializer,
                          CategoryPostSerializer,
                          OrganizationSerializer,
                          OrganizationPostSerializer,
                          PostsSerializer,
                          PostsPostSerializer,
                          TagSerializer,
                          TagPostSerializer,

                          )


class PostApiView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [TokenAuthentication, ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostsSerializer
        else:
            return PostsPostSerializer


class AuthorApiView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AuthorSerializer
        else:
            return AuthorPostSerializer


class OrganizationApiView(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return OrganizationSerializer
        else:
            return OrganizationPostSerializer


class TagApiView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TokenAuthentication, ]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return TagSerializer
        else:
            return TagPostSerializer


class CategoryApiView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TokenAuthentication, ]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CategorySerializer
        else:
            return CategoryPostSerializer
