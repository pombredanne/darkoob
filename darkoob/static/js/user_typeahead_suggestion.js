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
