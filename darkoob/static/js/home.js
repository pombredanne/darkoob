$(".deadline").children('a').bind("click", function () {
  span = $(this).parent().children('span');
  span.slideToggle(5000);
  //span.slideToggle('slow');
});

