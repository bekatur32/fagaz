import stripe
from django.conf import settings
from django.shortcuts import render
from django.views import View

stripe.api_key = settings.STRIPE_SECRET_KEY

class PaymentView(View):
    def get(self, request):
        return render(request, 'payment/payment.html')

    def post(self, request):
        token = request.POST.get('stripeToken')
        amount = 1000

        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                source=token
            )
        except stripe.error.CardError as e:
            error_message = e.error.message
            return render(request, 'payment/payment.html', {'error_message': error_message})

        return render(request, 'payment/success.html')