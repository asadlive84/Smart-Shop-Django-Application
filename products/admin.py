from django.contrib import admin
from products.models import ProductCategory, Product, ProductTag, ProductUnit

admin.site.register(Product)
admin.site.register(ProductUnit)
admin.site.register(ProductTag)
admin.site.register(ProductCategory)