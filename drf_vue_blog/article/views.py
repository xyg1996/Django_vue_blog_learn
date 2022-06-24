from django.http import JsonResponse
from article.models import Article
# 这个 ArticleListSerializer 暂时还没有

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.http import Http404

from article.models import Article

from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from article.permissions import IsAdminUserOrReadOnly
# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleDetailSerializer
#     permission_classes = [IsAdminUserOrReadOnly]

# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleListSerializer
#     permission_classes = [IsAdminUserOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

from rest_framework import viewsets
from article.serializers import ArticleSerializer
from django_filters.rest_framework import DjangoFilterBackend

from article.models import Tag
from article.serializers import TagSerializer

from article.models import Category
from article.serializers import CategorySerializer

from article.serializers import CategorySerializer, CategoryDetailSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """分类视图集"""
    ...
    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        else:
            return CategoryDetailSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """分类视图集"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author__username', 'title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
