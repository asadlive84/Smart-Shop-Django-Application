from django.db import models
from users.models import CustomUser


class ShopInfo(models.Model):
    created_by = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField("Shop Name", max_length=200)
    address = models.TextField("Address", blank=True, null=True)
    contact = models.CharField("Contact", max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

