$(".deadline").children('a').bind("click", function () {
  span = $(this).parent().children('span');
  span.toggle();
  //span.slideToggle('slow');
});

