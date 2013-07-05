$("#author-look").typeahead({
  source: function(query, process) {
    $.ajax({
      url: "/book/author/",
        data: {query: query},
        success: process,
      });
    },
  highlighter: function(item) {
    return item;
  },
});