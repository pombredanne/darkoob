$(document).ready(function() {
  $('.noks').tooltip({
    title: 'Nok',
    placement: 'right',
  });
});

function callback_nok_post(data) {
  if (data.ok) {
    $('#id_post_id_' + data.pid + ' .noks span').html(data.noks);
  } else {
    $.pnotify({
      title: 'Noking failed!',
      text: 'Please try again later',
      opacity: .8,
      type: 'info',
    });
  }
}


