from django.db import models
from django.conf import settings


class ProductCategory(models.Model):
    """
    This Table about product category
    """
    name = models.CharField(max_length=200)
    short_desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class ProductTag(models.Model):
    """
    This Table ProductTag about product tag
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Vendor(models.Model):
    """
    This Table about Vendor Information
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=100)
    short_info = models.TextField(blank=True, null=True)
    address = models.TextField("Address", blank=True, null=True)
    contact = models.CharField("Contact", max_length=200)

    def __str__(self):
        return f"{self.name}"


class ProductUnit(models.Model):
    """
    Product Unit: product unit, vendor, price
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    short_name = models.CharField("Short Name", max_length=100, blank=True, null=True)
    short_info = models.CharField("Short Information", max_length=100, blank=True, null=True)
    long_info = models.TextField("Long Information", blank=True, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField("Description", max_length=100, blank=True, null=True)
    unit = models.PositiveIntegerField("Unit")
    whole_sale_price = models.FloatField("Whole Sale Price")
    customer_price = models.FloatField("Customer Price")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.unit}"


class Product(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField("Product Name", max_length=100, db_index=True)
    category = models.ManyToManyField(ProductCategory)
    image = models.ImageField("Image", upload_to="product/", blank=True, null=True)
    description = models.TextField("Product Description", blank=True, null=True)
    tag = models.ManyToManyField(ProductTag, blank=True)
    unit = models.PositiveIntegerField("Unit", blank=True, null=True)
    in_stock = models.BooleanField("Stock", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['-created_at']
