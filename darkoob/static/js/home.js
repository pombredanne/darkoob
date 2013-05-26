$(".deadline").children('a').bind("click", function () {
  span = $(this).parent().children('span');
  if (span.css('display') == 'none') {
    span.css('display', 'block');
  } else if (span.css('display') == 'block') {
    span.css('display', 'none');
  } else if (!span.css('display')) {
    span.css('display', 'none');
  }
});

