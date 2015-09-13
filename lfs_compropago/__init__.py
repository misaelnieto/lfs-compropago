# django imports
from django.conf import settings

# lfs imports
from lfs.plugins import PaymentMethodProcessor
from lfs.plugins import PM_ORDER_IMMEDIATELY

from compropago import CompropagoAPI, Charge


class CompropagoMethodProcessor(PaymentMethodProcessor):
    def process(self):
        from lfs.core.utils import get_default_shop
        shop = get_default_shop(self.request) 
        api = CompropagoAPI(settings.LFS_COMPROPAGO_PUBLIC_API_KEY)
        c = Charge(
            product_price = self.order.price,
            product_name = shop.name,
            product_id = str(self.order.number),
            customer_name = order.user.first_name + order.user.last_name,
            customer_email = order.user.email,
            payment_type = "OXXO"
        )
        resp = api.charge(c)

        return {
            "accepted": True,
            "next_url": "http://www.acme.com/payment?id=4711&total=%s" % total,
        }

    def get_create_order_time(self):
        return PM_ORDER_ACCEPTED

    def get_pay_link(self):
        total = self.order.price
        return "http://www.acme.com/payment?id=4711&total=%s" % total
