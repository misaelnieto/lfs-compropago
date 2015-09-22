# django imports
from django.conf import settings

# lfs imports
from lfs.plugins import PaymentMethodProcessor
from lfs.plugins import PM_ORDER_IMMEDIATELY

from compropago import CompropagoAPI, CompropagoCharge


class CompropagoMethodProcessor(PaymentMethodProcessor):
    def process(self):
        from lfs.core.utils import get_default_shop
        shop = get_default_shop(self.request)
        api = CompropagoAPI(settings.LFS_COMPROPAGO_PUBLIC_API_KEY)
        order = self.order
        c = CompropagoCharge(
            order_id = str(order.number),
            order_price = order.price,
            order_name = shop.name,
            image_url = 'https://getfedora.org/static/images/fedora_infinity_140x140.png',
            customer_name = order.user.get_full_name() or order.user.email,
            customer_email = order.user.email,
            payment_type = "OXXO"
        )
        resp = api.charge(c)

        return {
            "accepted": True,
            "next_url": "http://www.acme.com/payment?id=4711&total=%s" % total,
        }

    def get_create_order_time(self):
        return PM_ORDER_IMMEDIATELY

    def get_pay_link(self):
        total = self.order.price
        return "http://www.acme.com/payment?id=4711&total=%s" % total
