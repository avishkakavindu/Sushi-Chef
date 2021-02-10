// payhere or cash on delivery
$("input[name='paymentmethod']").change(function(){
    if($(this).val() === 'payhere'){
        $('.cod-btn').empty()
        $('.ph-btn').empty().append(
            '<button type="submit" class="btn btn-success btn-block payhere-payment" id="payhere-payment" name="checkout_btn">proceed to pay</button>'
        )
    }
    else{
        $('.ph-btn').empty()
        $('.cod-btn').empty().append(
            '<button type="submit" class="btn btn-success btn-block" name="checkout_btn">Place Order</button>'
        )
    }
})

// show alert
function showAlert(msg){
         $('#payhere-alert').html('<div class="alert alert-warning alert-dismissible fade show" id="payhere-alert" role="alert">\n' +
             '                <p id="msg">'+msg+'</p>\n' +
             '              <button type="button" class="close" data-dismiss="alert" aria-label="Close">\n' +
             '                <span aria-hidden="true">&times;</span>\n' +
             '              </button>\n' +
             '            </div>');
         $('#alert').show();
        }


