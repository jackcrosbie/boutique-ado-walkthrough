from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe

def webhook(request):
    """ Listen to webhooks from Stripe """
    # setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_event(
        payload, sig_header, wh_secret 
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invaild Signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400 )

    print('success')
    return HttpResponse(status=200)
    