$(".deadline").children('a').bind("click", function () {
  span = $(this).parent().children('span');
  span.slideToggle(5000);
  //span.slideToggle('slow');
});

function set_my_quote_callback(data){
  if (data.done){
    $.pnotify({
      title: 'Profile Updated',
      text: data.message,
      opacity: .8
    })
  }else{
    for (i in data.errors){
      $.pnotify({
        title: 'Error',
        type:'error',
        text: data.errors[i],
        opacity: .8
      })
    }
  }
}

function submit_private_key_callback(data){
  if (data.done){
    $.pnotify({
      type: 'success',
      title: 'correct info',
      text: data.message,
      opacity: .8
    })
  }else{
    for (i in data.errors){
      $.pnotify({
        title: 'Error',
        type:'error',
        text: data.errors[i],
        opacity: .8
      })
    }
  }
}

//TODO: It's very dirty code
function close_1(){
  $('#follow_suggestion_1').remove();
}

function close_2(){
  $('#follow_suggestion_2').remove();
}

function close_3(){
  $('#follow_suggestion_3').remove();
}

function follow_request_callback_1(data){
  alert(data.done);
  close_1();
}

function follow_request_callback_2(data){
  alert(data.done);
  close_2();
}

function follow_request_callback_3(data){
  alert(data.done);
  close_3();
}

