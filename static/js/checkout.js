// payhere or cash on delivery
$("input[name='paymentmethod']").change(function(){
    if($(this).val() === 'payhere'){
        $('.cod-btn').empty()
        $('.ph-btn').empty().append(
            '<button type="submit" class="btn btn-success btn-block" id="payhere-payment" name="checkout_btn">proceed to pay</button>'
        )
    }
    else{
        $('.ph-btn').empty()
        $('.cod-btn').empty().append(
            '<button type="submit" class="btn btn-success btn-block" name="checkout_btn">Place Order</button>'
        )
    }
})


