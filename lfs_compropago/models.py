from django.conf import settings
from django.db import models

from lfs.order.models import Order

class CompropagoCurrencyConversion(models.Model):
    class Meta:
        db_table = 'lfs_compropago_currency_conversion'
    currency_code = models.CharField(max_length=4)
    rate = models.DecimalField(max_digits=64, decimal_places=3)
    created = models.DateTimeField(auto_now_add=True)


class CompropagoTransaction(models.Model):
    PAYMENT_TYPE_CHOICES = (
        ("OXXO", "Oxxo"),
        ("SEVEN_ELEVEN", "Seven Eleven"),
        ("EXTRA", "Extra"),
        ("CHEDRAUI", "Chedraui"),
        ("ELEKTRA", "Elektra"),
        ("COPPEL", "Coppel"),
        ("FARMACIA_BENAVIDES", "Farmacia Benavides"),
        ("FARMACIA_ESQUIVAR", "Farmacia Esquivar"),
    )
    """A transaction with compropago gateway"""
    class Meta:
        db_table = 'lfs_compropago_transaction'

    order = models.ForeignKey(Order, unique=True)
    payment_type = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255)
    short_payment_id = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=32)
    creation_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    product_information = models.TextField()
    payment_instructions = models.TextField()
    verified = models.BooleanField(default=False)

