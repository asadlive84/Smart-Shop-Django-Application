from rest_framework import serializers

from products.models import Product, ProductCategory, ProductTag, ProductUnit, Vendor


class ProductSerializer(serializers.ModelSerializer):
    product = serializers.HyperlinkedRelatedField(many=True,
                                                  read_only=True,
                                                  view_name='unit_detail')
    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name')

    class Meta:
        model = Product
        fields = ['created_by', 'name', 'category', 'image', 'description', 'in_stock', 'product', 'unit', 'created_at']


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


class ProductTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTag
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class ProductUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductUnit
        fields = '__all__'
