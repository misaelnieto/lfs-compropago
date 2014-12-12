# python imports
import locale

# lfs imports
from lfs.plugins import PaymentMethodProcessor
from lfs.plugins import PM_ORDER_IMMEDIATELY
from lfs.caching.utils import lfs_get_object_or_404
from lfs.core.models import Shop

class PayPalProcessor(PaymentMethodProcessor):
    def process(self):
        pass

    def get_create_order_time(self):
        return PM_ORDER_IMMEDIATELY

    def get_pay_link(self):
        return 'hola'
