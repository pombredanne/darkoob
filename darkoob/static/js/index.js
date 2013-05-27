$(document).ready(function() {
  $("#id_username").focus();
})

$("#id_signup_form").bind('submit', function() {
/*
  var validator = $("#id_signup_form").validate({
    rules: {
      confirm_password: { equalTo: '#id_password' }
    },
    messages: {
      confirm_password: { equalTo: "wroong man!" }
    },
  });
*/
  return false;

  if ($("#id_password").val() == $("#id_confirm_password")) {
    return true;
  } else {
    return false;
    $("#id_form_error").css("display", "block");
  }
})

function reset_form() {
  $("#id_signup_form")[0].reset();
}
