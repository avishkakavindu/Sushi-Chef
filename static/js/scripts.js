// change image -product
$(".sub-img").click(function(){
    sub_url = $(this).find('img').attr('src');
    $(this).find('img').attr('src', $('.main-img').find('img').attr('src'));
    $('.main-img').find('img').attr('src', sub_url);
})

// alerts auto close
$(document).ready(function() {
    // show the alert
    setTimeout(function() {
        $(".alert").alert('close');
    }, 2000);
});



