from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """ context processor, make dict available across entire app"""

    """ empty list for bag items to live in"""
    bag_items = []
    """ initialise total and product count to zero """
    total = 0
    product_count = 0
    """ getting bag if already exists or initialising to empty dict. if doesn't """
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    """ working out if free delivery or not """
    if total < settings.FREE_DELIVERY_THRESHOLD:
        """ using decimal as it's a financial transaction """
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        """ let users know how much more they need to spend for free delivery """
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
