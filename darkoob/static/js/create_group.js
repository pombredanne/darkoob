function duplicat_group (data) {
  if(data.is_exist) {
    $.pnotify({
      title: 'Duplicated Group',
      text: 'This group is already exist',
      type: 'info',
      opacity: .8
    });
    return false;
  }
  return true;
}
function load_members(){
  var member_list = ''

  $('.media').each(function(){
    member_list+=$(this).attr('id') + ',';
  })
  $('#id_members').val(member_list);
  Dajaxice.darkoob.group.is_group_exist(duplicat_group, {'group_name': $('#id_name').val()});
}

$(document).ready(function() {

  $(function(){

    var bondObjs = {};
    var bondNames = [];

      //get the data to populate the typeahead (plus an id value)
      var throttledRequest = _.debounce(function(query, process){
        //get the data to populate the typeahead (plus an id value)
        $.ajax({
          url: '/group/look'
          ,type: "GET"
          ,data: { query: $('#user-look').val()}
          ,cache: false
          ,success: function(data){
            //reset these containers every time the user searches
            //because we're potentially getting entirely different results from the api
            bondObjs = {};
            bondNames = [];

            //Using underscore.js for a functional approach at looping over the returned data.
            _.each( data, function(item, ix, list){

              //for each iteration of this loop the "item" argument contains
              //1 bond object from the array in our json, such as:
              // { "id":7, "name":"Pierce Brosnan" }

              //add the label to the display array
              bondNames.push( item.username );

              //also store a hashmap so that when bootstrap gives us the selected
              //name we can map that back to an id value
              bondObjs[ item.username ] = item;
            });

            //send the array of results to bootstrap for display
            process( bondNames );
          }
        });
});


$(".typeahead").typeahead({
  source: function ( query, process ) {

          //here we pass the query (search) and process callback arguments to the throttled function
          throttledRequest( query, process );

        }
        ,highlighter: function( item ){
          var bond = bondObjs[ item ];
          
          return '<div class="bond">'
          + "<div class='typeahead_wrapper'>"
          +'<img class=\'typeahead_photo\' src="' + bond.photo + '" />'
          + "<div class='typeahead_labels'>"
          +'<div class=\'typeahead_primary\'>' + bond.username + '</div>'
          + "<div class='typeahead_secondary'>" + bond.full_name + "</div>"
          +'</div>'
          +'</div>';
        }
        , updater: function ( selectedName ) {

          //note that the "selectedName" has nothing to do with the markup provided
          //by the highlighter function. It corresponds to the array of names
          //that we sent from the source function.

          //save the id value into the hidden field
          $( "#user-look" ).val( bondObjs[ selectedName ].id );

          //return the string you want to go into the textbox (the name)
          return selectedName;
        }
      });
});
});

function close_added_user(added_user)
{
  $(added_user).remove();

}

function is_in_added_users(username)
{
  var result = false
  if($('#added-users').children().length > 0) {
    $('#added-users').children().each(function(index, user) {
      if (user.id == username) {
        result = true;
      }
    });
  }
  return result;
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
$('#user-look').keypress(function(e) {
  if(e.which == 13) {
    Dajaxice.darkoob.social.is_user(is_user_callback, {'username': $('#user-look').val()});
  }
});
