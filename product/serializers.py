from rest_framework import serializers
from .models import Category, Product, ProductImage

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
    def to_representation(self, instance):
        return super().to_representation(instance)
        repr['images'] = ProductImg(instance.images.all(), many = True).data
        repr['category'] = CategorySerializer(instance.category).data['title']
        return repr
    
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title', 'image', 'price', 'category'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)

class ProductImg(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = 'image',
        
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'