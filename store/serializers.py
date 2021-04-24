from rest_framework import serializers
from .models import Product, Category, Profile



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['product', 'avatar']


class ProductSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Product.STATUS_CHOICES)
    timestamp = serializers.DateTimeField(format=("%Y-%m-%d %H:%M:%S"))
    product_images = ProfileSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id', 'title', 'slug', 'description', 'price', 'timestamp',
         'seller', 'status', 'category', 'product_images')


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'products')
