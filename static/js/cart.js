var updateBtns = document.getElementsByClassName('update-cart');

for(var i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:', productId, 'action: ',action);

        updateCartItems(productId, action);
    })
}

// do changes to cart items
function updateCartItems(productId, action){
    if(action == 'add'){
        if(cart[productId] == undefined){       // if the product not in cart
            cart[productId] = {'quantity': 1}   // ex: {1: {'quantity': 1}}
        }
        else {                                  // if product is already in cart increment quantity
            cart[productId]['quantity'] += 1
        }
    }
    else if(action == 'remove'){
        if(cart[productId][quantity] > 0){
            cart[productId][quantity] -= 1
        }
        else {
            delete cart[productId]
        }
    }
    // set the updated cookie
    document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/'
    console.log(cart)
}