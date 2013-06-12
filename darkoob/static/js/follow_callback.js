function follow_person_in_user_page_callback(data){
  if (data.done){
    $('#follow_btn_'+data.user_id).attr('class','btn btn-success btn-primary disabled')
    $('#follow_btn_'+data.user_id).attr('disabled', 'disabled')
    $.pnotify({
      title: 'Follow',
      text: 'Added to your following list',
      type:'success',
      opacity: .8
    })
  }else{
    $.pnotify({
      title: 'Follow',
      text: 'An error occured.please try again',
      type:'error',
      opacity: .8
    })
  }
}
