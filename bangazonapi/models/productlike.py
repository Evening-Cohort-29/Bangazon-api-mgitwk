from django.db import models
from .product import Product
from .customer import Customer


class ProductLike(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="likes")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="likes"
                                )

    class Meta:
        # We don't want a customer to be able to like the same product multiple times. unique_together prevents duplicate rows in a table based on a combination of fields.
        unique_together = ['customer', 'product']
