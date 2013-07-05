function duplicat_book (data) {   ///FIX IT
  if(data.is_exist) {
    $.pnotify({
      title: 'Duplicated Group',
      text: 'This group is already exist',
      type: 'info',
      opacity: .8
    });
    return false;
  }
  $('#add_group_form').submit()
  return true;
}




function is_user_callback(data)
{
  if (data.is_exist ) {
    if (!is_in_added_users($('#user-look').val())) {
      $('#added-users').append(
        '<div class="media" id="'+ $('#user-look').val() +'" >' +
        '<a class="pull-left" href="#">' +
        '<img class="media-object" src="'+ data.url +'">'+
        '</a><div class="media-body">' +
        '<button class="close" id="close_button" onmousedown="close_added_user(\'#'+$('#user-look').val()+'\')">&times;</button>'+
        '<b class="media-heading">'+ $('#user-look').val() +'</b><br/>' +
        data.full_name +
        '</div>' +
        '</div>'
        )
    } else {
      $.pnotify({
        title: 'Duplicated Username',
        text: 'This user is already added',
        type: 'info',
        opacity: .8
      });
    }
  } else {
    $.pnotify({
      title: 'Not Exist',
      text: 'Wrong username , be sure what you looking for!',
      type: 'error',
      opacity: .8
    });
  }
}
$('#book-look').keypress(function(e) {
  if(e.which == 13) {
    Dajaxice.darkoob.group.is_book(is_user_callback, {'username': $('#user-look').val()});
  }
});
