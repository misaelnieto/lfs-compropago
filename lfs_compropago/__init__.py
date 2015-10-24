import json
from datetime import datetime
# django imports
from django.conf import settings
from django.core.urlresolvers import reverse
from dateutil.parser import parse as parse_date

# lfs imports
from lfs.plugins import PaymentMethodProcessor
from lfs.plugins import PM_ORDER_IMMEDIATELY

from compropago import CompropagoAPI, CompropagoCharge


class CompropagoMethodProcessor(PaymentMethodProcessor):
    def process(self):
        from lfs.core.utils import get_default_shop
        from .models import CompropagoTransaction
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

        r = api.charge(c)

        tx = CompropagoTransaction(
            order = self.order,
            payment_type = 'OXXO',
            payment_id = r['payment_id'],
            short_payment_id = r['short_payment_id'],
            payment_status = r['payment_status'],
            creation_date = parse_date(r['creation_date'], ignoretz=True),
            expiration_date = parse_date(r['expiration_date'], ignoretz=True),
            updated_date = datetime.now(),
            product_information = json.dumps(r['product_information']),
            payment_instructions = json.dumps(r['payment_instructions']),
        )
        tx.save()
        return {
            "accepted": True,
            "next_url": reverse('compropago_instrucciones', args=[tx.pk])
        }

    def get_create_order_time(self):
        return PM_ORDER_IMMEDIATELY

    def get_pay_link(self):
        total = self.order.price
        return "http://www.acme.com/payment?id=4711&total=%s" % total
