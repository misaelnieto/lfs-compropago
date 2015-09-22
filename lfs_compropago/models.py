from django.db import models

from lfs.order.models import Order


class CompropagoTransaction(models.Model):
    """A transaction with compropago gateway"""

    VALID_PAYMENT_STATUS_CHOICES = (
        ('charge.pending', 'Pending'),
        ('charge.success', 'Success')
    )
    order = models.ForeignKey(Order, unique=True)
    payment_id = models.CharField(max_length=255)
    short_payment_id = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=32, choices=VALID_PAYMENT_STATUS_CHOICES)
    creation_date = models.DateField()
    expiration_date = models.DateField()
    product_information = models.TextField()
    payment_instructions = models.TextField()
    verified = models.BooleanField(default=False)

