function group_toggle_cb(data) {
  if (data.error.title) {
    $.pnotify({
      title: data.error.title,
      text: data.error.text,
      opacity: .8,
      type: 'error',
    });
  } else {
    if (data.is_member) {
      $('#group-toggle-btn').html('Leave');
    } else {
      $('#group-toggle-btn').html('Join');
    }
  }
}
