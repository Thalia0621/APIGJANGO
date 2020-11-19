from rest_framework import serializers
from .models import categories
from .models import customers
from .models import products
from .models import order
from .models import orderDetail

class categories_serializer(serializers.ModelSerializer):
    class Meta:
        model=categories
        fields='__all__'


class customers_serializer(serializers.ModelSerializer):
    class Meta:
        model=customers
        fields='__all__'

class products_serializer(serializers.ModelSerializer):
    class Meta:
        model=products
        fields='__all__'

class order_serializer(serializers.ModelSerializer):
    class Meta:
        model=order
        fields='__all__'

class orderdetail_serializer(serializers.ModelSerializer):
    class Meta:
        model=orderDetail
        fields='__all__'