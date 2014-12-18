/*
	Add to cart fly effect with jQuery. - May 05, 2013
	(c) 2013 @ElmahdiMahmoud - fikra-masri.by
	license: http://www.opensource.org/licenses/mit-license.php
*/
(function($, window, undefined) {
  "use strict";
    $(document).ready(function() {

        $('.add-to-cart').on('click', function () {
            var cart = $('.shopping-cart');
            var imgtodrag = $(this).parent('.gallery_items').find("img").eq(0);
            if (imgtodrag) {
                var imgclone = imgtodrag.clone()
                    .offset({
                    top: imgtodrag.offset().top,
                    left: imgtodrag.offset().left
                })
                    .css({
                    'opacity': '0.5',
                        'position': 'absolute',
                        'height': '150px',
                        'width': '150px',
                        'z-index': '9999999'
                })
                    .appendTo($('body'))
                    .animate({
                    'top': cart.offset().top + 20,
                        'left': cart.offset().left + 20,
                        'width': 75,
                        'height': 75
                }, 1000, 'swing');

                setTimeout(function () {
                    cart.effect("shake", {
                        times: 2
                    }, 200);
                }, 1500);

                imgclone.animate({
                    'width': 0,
                        'height': 0
                }, function () {
                    $(this).detach()
                });
            }
        });
    });

}(jQuery, window));