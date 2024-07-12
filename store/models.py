from django.db import models
from django.contrib.auth.models import User

class StoreCategory(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'store_categories'
        verbose_name = 'Store Category'
        verbose_name_plural = 'Store Categories'

    def __str__(self):
        return self.name

class StoreProduct(models.Model):
    category = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    picture = models.ImageField(upload_to='uploads/store/products/')
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'store_products'
        verbose_name = 'Store Product'
        verbose_name_plural = 'Store Products'

    def __str__(self):
        return self.name

class StoreOrder(models.Model):
    address = models.CharField(max_length=255)
    amount_paid = models.DecimalField(decimal_places=2, max_digits=6)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    delivered = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'store_orders'
        verbose_name = 'Store Order'
        verbose_name_plural = 'Store Orders'

    def __str__(self):
        return f'Order {self.id}'

class StoreOrderItem(models.Model):
    order = models.ForeignKey(StoreOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(StoreProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'store_order_items'
        verbose_name = 'Store Order Item'
        verbose_name_plural = 'Store Order Items'

    def __str__(self):
        return f'Order Item {self.id}'


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=255, unique=True)
    merchant_order_id = models.CharField(max_length=255, null=True, blank=True, default=None)
    def __str__(self):
        return self.user.username