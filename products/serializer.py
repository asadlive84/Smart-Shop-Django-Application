from rest_framework import serializers

from products.models import Product, ProductCategory, ProductTag, ProductUnit


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id',
                  'name',
                  'image',
                  'description',
                  'unit',
                  'in_stock',
                  'created_at',
                  'updated_at',
                  'category',
                  'tag']


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTag
        fields = "__all__"


class ProductUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductUnit
        fields = '__all__'
