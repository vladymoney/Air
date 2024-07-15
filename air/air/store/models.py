from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_code = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=100)
    primary_image = models.URLField(max_length=200)  # Primary image URL
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.url

class Cart(models.Model):
    session_id = models.CharField(max_length=32)
    # other fields

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Favorite(models.Model):
    session_id = models.CharField(max_length=32)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
