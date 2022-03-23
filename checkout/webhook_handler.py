from django.http import HttpResponse

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    # init class is a setup method, called everytime
    def __init__(self, request):
        self.request = request

    # this will take the event stripe is sending us
    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        # return http response to show the event was received
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
    def __init__(self, request):
        self.request = request

    # this will take the event stripe is sending us
    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        # return http response to show the event was received
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
    def __init__(self, request):
        self.request = request

    # this will take the event stripe is sending us
    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        # return http response to show the event was received
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
    def __init__(self, request):
        self.request = request
    
    
    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        # return http response to show the event was received
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
    def __init__(self, request):
        self.request = request

 