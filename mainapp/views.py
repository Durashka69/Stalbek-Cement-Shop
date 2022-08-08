from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend

from mainapp.models import Category, Product, Raiting
from mainapp.serializers import CategorySerializer, ProductSerializer, RaitingSerializer
from mainapp.filters import CategoryFilter, ProductFilter
from mainapp.permissions import IsOwnerOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class RaitingViewSet(viewsets.ModelViewSet):
    queryset = Raiting.objects.all()
    serializer_class = RaitingSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
