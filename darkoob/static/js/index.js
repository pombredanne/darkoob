function validate_signup() {
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

  if ($("#id_password").val() == $("#id_confirm_password")) {
    return;
  } else {
    highlight
}
