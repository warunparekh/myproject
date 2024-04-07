from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True , default='products/face_wash.webp')  # Optional image field
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_data = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # Discount as a decimal percentage

    def __str__(self):
        return self.name
