(function ($) {
    "use strict";

    // Initiate the wowjs
    new WOW().init();


$(document).ready(function () {
    $(".testimonial").slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      infinite: true,
      arrows: false,
      draggable: false,
      dots: true,
      responsive: [
        {
          breakpoint: 1025, // Độ rộng thiết bị
          settings: {
            slidesToShow: 1,
          },
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            arrows: false, // Ẩn nút kéo
            infinite: false, // Kéo tới cuối không kéo dc nữa
          },
        },
      ],
      autoplay: true,
      autoplaySpeed: 3000,
    });
  });
})(jQuery);

