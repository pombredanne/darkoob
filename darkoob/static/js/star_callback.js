function star_book_callback(data){
  if (data.done){
    $('#star_btn_'+data.book_id).attr('class','btn btn-success btn-primary disabled')
    $('#star_btn_'+data.book_id).attr('disabled', 'disabled')
    $.pnotify({
      title: 'Favorite',
      text: 'This book added to your favorite book',
      type:'success',
      opacity: .8
    })
  }else{
    $.pnotify({
      title: 'Favorite',
      text: 'An error occured.please try again',
      type:'error',
      opacity: .8
    })
  }
}
