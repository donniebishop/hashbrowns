// justify tabs for md-width viewport
$(window).on('resize', function () {
  var win = $(this);
  if (win.width() < 768 || win.width() > 992) {
     $('#tab_list').removeClass('nav-justified')
  }
 else{
  $('#tab_list').addClass('nav-justified')};
});
