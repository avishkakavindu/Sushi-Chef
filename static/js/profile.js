// profile pic upload btn
$(".upload-icon").click(function () {
    $("input[type='file']").trigger('click');


  });
// preview
id_profile_pic.onchange = function (event) {
    frame.src=URL.createObjectURL(event.target.files[0]);
}