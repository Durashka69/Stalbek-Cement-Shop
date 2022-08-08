from django_filters import rest_framework as filters

from mainapp.models import Product, Category


class CategoryFilter(filters.FilterSet):
    class Meta:
        model = Category
        fields = ('title',)


class ProductFilter(filters.FilterSet):
    price_from = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_to = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ('title', 'price_from', 'price_to',)
