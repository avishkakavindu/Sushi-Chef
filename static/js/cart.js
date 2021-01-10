var updateBtns = document.getElementsByClassName('update-cart');

for(var i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){

        event.preventDefault();
        var [productId, unitPrice, product_name] = this.dataset.product.split('_');
        var action = this.dataset.action;

        updateCartItems(productId, unitPrice, action);

        $('#added-to-cart').append("<div class='alert alert-success alert-dismissable msg'><button type='button' class='close ml-1' data-dismiss='alert' aria-hidden='true'>&times;</button><i class='fa fa-check-circle-o fa-lg mr-4' aria-hidden='true'></i>"+ product_name +" added to cart successfully</div>")
    })
}

// do changes to cart items
function updateCartItems(productId, unitPrice, action){
    if(action == 'add'){

        if(cart[productId] == undefined){       // if the product not in cart
            cart[productId] = {
                'unit_price': unitPrice,
                'quantity': 1
                }   // ex: {1: {'quantity': 1}}
            // console.log('undef')
        }
        else {                                  // if product is already in cart increment quantity
            cart[productId]['quantity'] += 1
            // console.log(cart[productId])
        }
    }
    else if(action == 'add-serving'){
        if(cart[productId] == undefined){       // if the product not in cart
            cart[productId] = {
                'unit_price': unitPrice,
                'quantity': parseInt($('.quantity').val())
                }   // ex: {1: {'quantity': 1}}
            console.log(parseInt($('.quantity').val()))
        }
        else {                                  // if product is already in cart increment quantity
            cart[productId]['quantity'] += parseInt($('.quantity').val())
            // console.log(cart[productId])
            console.log(parseInt($('.quantity').val()))
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
        calcSummary()
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
            calcSummary()
        }
        else{
            cart[productId]['quantity'] = $(this).val()
            cost = '$' + String(parseFloat(cart[productId]['quantity'] * unitPrice).toFixed(2))
            $(this).closest('.cart-item').children('.cost-container').children('.cost').text(cost)
            calcSummary()
        }
        // set the updated cookie
        document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/'
        console.log(JSON.stringify(cart))

    })
})


// calculate total and sub total
function calcSummary(){
    var sum = 0;
    $('.cost').each(function() {
        sum += parseFloat($(this).text().replace('$', ''));
        $(".sub-total").text('$' + sum.toFixed(2));
        $('.total').text('$' + (sum + 5).toFixed(2))
    });
}


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

// add to wish list
$('.addto-wish').click(function(e){
    var dishid;
    dishid = $(this).attr("data-product");
    $(this).find('.fa').removeClass('fa-heart-o')
    $(this).find('.fa').addClass('fa-heart');
    e.preventDefault();
    $.ajax(
        {
            type:"GET",
            url: "/wishlist",
            data:{
                     dish_id: dishid
            },
            success: function( data )
            {

                $('#added-to-cart').append("<div class='alert alert-success alert-dismissable msg'><button type='button' class='close ml-1' data-dismiss='alert' aria-hidden='true'>&times;</button><i class='fa fa-check-circle-o fa-lg mr-4' aria-hidden='true'></i>"+ data + "</div>")
            },
            error: function(data)
            {
                $('#added-to-cart').append("<div class='alert alert-danger alert-dismissable msg'><button type='button' class='close ml-1' data-dismiss='alert' aria-hidden='true'>&times;</button><i class='fa fa-check-circle-o fa-lg mr-4' aria-hidden='true'></i>"+ data + "</div>")
            }
         })
});