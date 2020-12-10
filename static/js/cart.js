var updateBtns = document.getElementsByClassName('update-cart');

for(var i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        event.preventDefault();
        var [productId, unitPrice] = this.dataset.product.split('_');
        var action = this.dataset.action;

        updateCartItems(productId, unitPrice, action);
    })
}

// do changes to cart items
function updateCartItems(productId, unitPrice, action){
    if(action == 'add'){
        if(cart[productId] == undefined){       // if the product not in cart
            cart[productId] = {'unit_price': unitPrice, 'quantity': 1}   // ex: {1: {'quantity': 1}}
        }
        else {                                  // if product is already in cart increment quantity
            cart[productId]['quantity'] += 1
        }
    }
    else if(action == 'remove'){
        if(cart[productId]['quantity'] > 0){
            cart[productId]['quantity'] -= 1
        }
        else {
            delete cart[productId]
        }
    }
    else if(action == 'delete'){
        delete cart[productId]
        console.log('delete: ')
    }
    // set the updated cookie
    document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/'

    // get item count in cart
     var cartItemCount = Object.keys(cart).length
     $('.cart-badge').text(cartItemCount)
}

// update quantity
$(function(){
    $('.cart-item .update-quantity').on('change', function(e){
        var [productId, unitPrice] = this.dataset.product.split('_');

        if ($(this).val() < 0){
            cart[productId]['quantity'] = parseInt(1)
            $(this).val(1)
            $(this).closest('.cart-item').children('.cost-container').children('.cost').text(unitPrice)
        }
        else{
            cart[productId]['quantity'] = $(this).val()
            cost = '$' + String(parseFloat(cart[productId]['quantity'] * unitPrice).toFixed(2))
            $(this).closest('.cart-item').children('.cost-container').children('.cost').text(cost)
            // calculate sub total
            var sum = 0;
            $('.cost').each(function() {
                sum += parseFloat($(this).text().replace('$', ''));
                $(".sub-total").text('$'+sum.toFixed(2));
            });
        }
        // set the updated cookie
        document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/'
        console.log(JSON.stringify(cart))

    })
})



// set quantity from cookie - replaced with django filter
//$(document).ready(function() {
//
//    $('.update-quantity').each(function(){
//        var [productId, unitPrice] = this.dataset.product.split('_');
//        $(this).val(cart[productId]['quantity']);
//        console.log($(this).val(cart[productId]['quantity']))
//    })
//})

// remove item from cart
$(function(){
  $("i.fa-trash").on('click', function(e) {
    $(this).parent().parent().parent().remove();
  });
});