from rest_framework import serializers
from shop.env.models import Product
from shop.env.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_name', 'price', 'product_type', 'image')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('mail', 'password', 'user_name')