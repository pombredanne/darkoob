function validate_signup() {
  var validator = $("#id_signup_form").validate({
    rules: {
      confirm_password: { equalTo: '#id_password' }
    },
    messages: {
      confirm_password: "wroong man!"
    }
  });
}
