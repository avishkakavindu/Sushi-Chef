import hashlib
from decouple import config
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from store.models import *


@csrf_exempt
def payhere(request):
    if request.method == 'POST':
        payload = request.POST
        merchant_id = payload.get('merchant_id')
        order_id = payload.get('order_id')
        payhere_amount = payload.get('payhere_amount')
        payhere_currency = payload.get('payhere_currency')
        status_code = payload.get('status_code')
        md5sig = payload.get('md5sig')
        custom_1 = payload.get('custom_1')
        custom_2 = payload.get('custom_2')
        method = payload.get('method')
        status_message = payload.get('status_message')
        card_holder_name = payload.get('card_holder_name')
        card_no = payload.get('card_no')
        card_expiry = payload.get('card_expiry')

        try:
            local_md5sig = hashlib.md5(
                merchant_id + order_id + payhere_amount + payhere_currency + status_code + hashlib.md5(
                    config('MERCHANT_SECRET')
                ).upper()).upper()

            if (local_md5sig == md5sig) and status_code == '2':
                order = Order.objects.get(id=order_id)
                payhere_record = PayherePaymentDetail(
                    merchant_id=merchant_id,
                    order_id=order,
                    payhere_amount=payhere_amount,
                    payhere_currency=payhere_currency,
                    method=method,
                    card_holder_name=card_holder_name,
                    card_no=card_no
                )
                payhere_record.save()
        except:
            messages.error(request, 'Payhere payment process failed!')
            HttpResponse('Failed')
