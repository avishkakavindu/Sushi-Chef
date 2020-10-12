var updateBtns = document.getElementsByClassName('update-cart');

// update cart items (quantity, newitems) 
for(i=0; i<updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        //console.log('productId: ', productId, ' | Action: ', action)
        
        updateUserOrder(productId, action);
        addCookieItem(productId, action);
    })
}

// Update current user order
function updateUserOrder() {
    console.log("Update user order request detected!");
}

// function addCookieItem(productId, action) {
//     console.log("XXXX: ", myCart);
//     if(action == 'add') {
//         if(myCart[productId] == undefined) {
//             myCart[productId] = {'quantity': 1};

//         }else {
//             myCart[productId]['quantity'] += 1;
//         }
//         console.log('addCookieItem: ', myCart);

//         console.log("---", myCart);
//     }
//     if(action == 'remove') {
//         myCart[productId]['quantity'] -= 1;

//         if(myCart[productId]['quantity'] <= 0) {
//             console.log('Item should be deleted!!!');
//             delete myCart[productId];
//         } 
//     }
//     console.log('My Cart:', myCart);
//     document.cookie = 'myCart=' + JSON.stringify(myCart) + ";domain=;path=/";
// }