from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_list_or_404, HttpResponse
from store.models import *
from store.decorators import allowed_user
from store.forms import UpdateCustomerForm, UpdateUserForm
from django.db.models import Prefetch
from SushiChef.myconfig import MERCHANT_SECRET
import hashlib


def payhere(request):
    if request.method == 'POST':
        payload = request.POST
        merchant_id = payload.get('merchant_id')
        order_id = payload.get('order_id')
        payhere_amount = payload.get('payhere_amount')
        payhere_currency = payload.get('payment_currency')
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
                    MERCHANT_SECRET
                ).upper()).upper()

            if (local_md5sig == md5sig) and status_code == '2':
                order = Order.objects.get(id=order_id)
                payhere_record = PayherePaymentDetail(
                    merchant_id=merchant_id,
                    order_id=order_id,
                    payhere_amount=payhere_amount,
                    payhere_currency=payhere_currency,
                    method=method,
                    card_holder_name=card_holder_name,
                    card_no=card_no
                )
                payhere_record.save()
        except:
            messages.error(request, 'Payhere payment process failed!')
