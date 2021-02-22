from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Product(models.Model):
    class PackageType(models.TextChoices):
        PREMIUM = 'PR', _('Premium')
        GOLD = 'GD', _('Gold')
        REGULAR = 'RG', _('Regular')
    package_type = models.CharField(max_length=2, choices=PackageType.choices, default=PackageType.REGULAR)    
    class ProductCategory(models.TextChoices):
        Men = 'M', _('Men Clothing')
        Women = 'W', _('Women Clothing')
        Children = 'C', _('Children Clothing')
    product_category = models.CharField(max_length=2, choices=ProductCategory.choices, default=ProductCategory.Men)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    details = models.TextField()
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    discount = models.FloatField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)


