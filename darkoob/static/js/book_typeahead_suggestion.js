$(document).ready(function() {
  $(function(){
    var bondObjs = {};
    var bondNames = [];

    var throttledRequest = _.debounce(function(query, process){
      $.ajax({
        url: '/book/look'
        ,type: "GET"
        ,data: { query: $('#title-look').val()}
        ,cache: false
        ,success: function(data){
          bondObjs = {};
          bondNames = [];
          _.each( data, function(item, ix, list){
            bondNames.push( item.book_title );
            bondObjs[ item.book_title ] = item;
          });
          process( bondNames );
        }
      });
    });

    $("#title-look").typeahead({
      source: function ( query, process ) {
        throttledRequest( query, process );
      }
      ,highlighter: function( item ){
        var bond = bondObjs[ item ];

        return '<div class="bond">'
        + "<div class='typeahead_wrapper'>"
        +'<img class=\'typeahead_photo\' src="' + bond.photo + '" />'
        + "<div class='typeahead_labels'>"
        +'<div class=\'typeahead_primary\'>' + bond.book_title + '</div>'
        + "<div class='typeahead_secondary'>" + bond.author_name + "</div>"
        +'</div>'
        +'</div>';
      }
      , updater: function ( selectedName ) {
        $( "#title-look" ).val( bondObjs[ selectedName ].id );
        return selectedName;
      }
    });
  });
});