import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {  # field name: ['query_lookup', ...]
            'name':['icontains', 'iexact']
        }
