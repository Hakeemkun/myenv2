
$(function() {
    $(".skill_box .skill_level span").each(function() {
      $(this).animate({
        width: $(this).data("width")
      }, 1000);
    });
  });
  
