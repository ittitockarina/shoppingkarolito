from django.db import models
from django.contrib.auth.models import User

class ShippingInformation(models.Model):
    address = models.CharField(max_length=255)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=40)

    class Meta:
        db_table = 'shipping_informations'
        verbose_name = 'Shipping Information'
        verbose_name_plural = 'Shipping Informations'

    def __str__(self):
        return self.address

class PaymentCard(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    cvc = models.CharField(max_length=3)
    date = models.CharField(max_length=5)
    number = models.CharField(max_length=19)

    class Meta:
        db_table = 'payment_cards'
        verbose_name = 'Payment Card'
        verbose_name_plural = 'Payment Cards'

    def __str__(self):
        return self.number
