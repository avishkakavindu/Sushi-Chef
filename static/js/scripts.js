$(document).ready(function(){
    // get item count in cart
    var cartItemCount = Object.keys(cart).length
    $('.cart-badge').text(cartItemCount)
})

// tooltips
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

// change image -product
$(".sub-img").click(function(){
    sub_url = $(this).find('img').attr('src');
    $(this).find('img').attr('src', $('.main-img').find('img').attr('src'));
    $('.main-img').find('img').attr('src', sub_url);
})

// alerts auto close
$(document).ready(function() {
    // close the alert
    setTimeout(function() {
        $(".alert").alert('close');
    }, 5000);
});


// get a cookie
function getCookie(cname){
    // get all name=value pairs in an array
    var cArr =document.cookie.split(';');
    for(var i=0; i<cArr.length; i++){
        var cPair = cArr[i].split('=');
        // remove white spaces and compare with cookie name
        if(cname == cPair[0].trim()){
            // decode cookie value and return
            return decodeURIComponent(cPair[1]);
        }
    }
    // if cookie not found
    return null;
}

var cart = JSON.parse(getCookie('cart'));
// if no cookie named 'cart'
if (cart == undefined){
    cart = {};
    console.log('Cart created', cart);
    document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/';
}

// get user
function getUser(){
    if($('.username').text() != undefined){
        return $('.username').text()
    }
    return '0'
}

// star rating system
$('.rate-me').mouseover(function(){

    $(this).prevAll().addBack().each(function(){
        $(this).removeClass('fa-star-o')
        $(this).addClass('fa-star')
        rating++

    })
    $(this).nextAll().each(function(){
        $(this).removeClass('fa-star')
        $(this).addClass('fa-star-o')
    })
    var rating = $('.rate-me.fa-star').length
    $('#id_rating').val(rating)
})
