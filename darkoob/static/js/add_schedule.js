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




function is_book_callback(data)
{
  alert(data)
}
$('#title-look').keypress(function(e) {
  if(e.which == 13) {
    Dajaxice.darkoob.book.is_book(is_book_callback, {'book_id': $('#title-look').attr('id')});
  }
});
