/*---------------------------------------------------------------------
    File Name: custom.js
----------------------------------------------------------------------- */

/* ---------------------------------------------------------------------
	
	* 1.  // Preloader *
	* 2.  // Flip Bar *
	* 3.  // Search form *
	* 4.  // Camera - Slider 01 *
	* 5.  // Camera - Slider 02 *
	* 6.  // Fixed menu *
	* 7.  // Main menu  *
	* 8.  // Project Slide *
	* 9.  // Testimonial Slider *
	* 10. // Partner Carousel *
	* 11. // Portfolio filters *
	* 12. // Scroll to top *
	* 13. // Scroll to top *
	* 14. // Parallax *
	* 15. // Placeholdem *
	* 16. // Image-scroll  *
	* 17. // Particles-js *
	
----------------------------------------------------------------------- */


(function($) {
    "use strict";
		
		/*---------------------------------------------------------------------
			Preloader
		-----------------------------------------------------------------------*/
		
		$(window).on('load', function() { 
			$('#loader').fadeOut(); 
			$('#preloader').delay(550).fadeOut('slow'); 
			$('body').delay(450).css({'overflow':'visible'});
		})
		
		/*---------------------------------------------------------------------
			Flip Bar
		-----------------------------------------------------------------------*/
		
		$(document).ready(function() {
			$(".flip").on('click',function() {
				$(".panel").slideToggle("slow");
			});
		});
		
		/*---------------------------------------------------------------------
			Search form
		-----------------------------------------------------------------------*/
		
		$('.search-icon').on('click',function(){
			$('.navbar-form').fadeIn(10);
			$('.navbar-form input').focus();
				});
			$('.navbar-form input').blur(function(){
				$('.navbar-form').fadeOut(10);
		});
		
		/*---------------------------------------------------------------------
			Camera - Slider 01
		-----------------------------------------------------------------------*/
		
		var banner = $(".slider-camera");
        if (banner.length) {
          banner.camera({ 
            height: '645px',
            pagination: false,
            navigation: true,
            thumbnails: false,
            playPause: false,
            pauseOnClick: false,
            autoPlay:true,
            hover: false,
            overlayer: true,
            loader: 'none',
            minHeight: '645px',
            time: 400000,
          });
        };
		
		/*---------------------------------------------------------------------
			Camera - Slider 02
		-----------------------------------------------------------------------*/
		
		var banner = $(".slider-camera-2");
        if (banner.length) {
          banner.camera({ 
            height: '790px',
            pagination: false,
            navigation: true,
            thumbnails: false,
            playPause: false,
            pauseOnClick: false,
            autoPlay:true,
            hover: false,
            overlayer: true,
            loader: 'none',
            minHeight: '790px',
            time: 400000,
          });
        };
		
		/*---------------------------------------------------------------------
			Fixed menu
		-----------------------------------------------------------------------*/
		
		$(window).on('scroll', function () {
			if ($(window).scrollTop() > 50) {
				$('.main-header-top').addClass('fixed-menu');
			} else {
				$('.main-header-top').removeClass('fixed-menu');
			}
		});
		
		/*---------------------------------------------------------------------
			Main menu
		-----------------------------------------------------------------------*/
		
		function mobileDropdown () {
		  if($('#mainNav').length) {
			$('#mainNav .nav li.dropdown-bcc').append(function () {
			  return '<i class="lnr lnr-chevron-down"></i>';
			});
			$('#mainNav .nav li.dropdown-bcc .lnr').on('click', function () {
			  $(this).parent('li').children('ul').slideToggle();
			});
		  }
		}

		jQuery(document).on('ready', function() {
		  mobileDropdown ();
		});
		
		/*---------------------------------------------------------------------
			Project Slide
		-----------------------------------------------------------------------*/
		
		$(".project-slider").owlCarousel({
            loop: true,
            dots: false,
            margin: 15,
            autoplay: true,
            autoplaySpeed: 4000,
            autoplayTimeout: 4000,
            autoplayHoverPause: true,
			navText: ["<span class='lnr lnr-chevron-left'></span>", "<span class='lnr lnr-chevron-right'></span>"],
            nav: true,
            responsive: {
                0:{
				items:1
				},
				767:{
					items:2
				},
				1000:{
					items:4
				}
            }
        });
		
		/*---------------------------------------------------------------------
			Testimonial Slider
		-----------------------------------------------------------------------*/
		
		$(".testimonial-slider").owlCarousel({
            loop: true,
            items: 1,
            dots: false,
            nav: false,
            autoplay: true,
            autoplaySpeed: 1000,
            autoplayTimeout: 3000,
            autoplayHoverPause: true
        });
		
		/*---------------------------------------------------------------------
			Partner Slider
		-----------------------------------------------------------------------*/
		
		$(".partner-slider").owlCarousel({
            loop: true,
            dots: false,
            margin: 15,
            autoplay: true,
            autoplaySpeed: 4000,
            autoplayTimeout: 4000,
            autoplayHoverPause: true,
            nav: false,
            responsive: {
                0:{
					items:1
				},
				599:{
					items:2
				},
				767:{
					items:3
				},
				991:{
					items:4
				},
				1000:{
					items:5
				}
            }
        });
		
		/*---------------------------------------------------------------------
			Portfolio filters
		-----------------------------------------------------------------------*/
		
        $(".project-menu span").on('click', function () {
            $(".project-menu span").removeClass('active');
            $(this).addClass('active');
            var filterValue = $(this).attr('data-filter');
            $(".project-gird").isotope({
                filter: filterValue
            });
        }); 		
		
		/*---------------------------------------------------------------------
			Scroll to top  
		-----------------------------------------------------------------------*/
		
		if ($('#scroll-to-top').length) {
			var scrollTrigger = 100, // px
				backToTop = function () {
					var scrollTop = $(window).scrollTop();
					if (scrollTop > scrollTrigger) {
						$('#scroll-to-top').addClass('show');
					} else {
						$('#scroll-to-top').removeClass('show');
					}
				};
			backToTop();
			$(window).on('scroll', function () {
				backToTop();
			});
			$('#scroll-to-top').on('click', function (e) {
				e.preventDefault();
				$('html,body').animate({
					scrollTop: 0
				}, 600);
			});
		}
		
		/*---------------------------------------------------------------------
			Parallax
		-----------------------------------------------------------------------*/
		
		$(document).ready(function(){
			$('.parallax').parallax("50%", 0.3);
			$('#parallax').parallax("50%", 0.3);
			$('#intro').parallax("50%", 0.3);
			$('#third').parallax("50%", 0.3);
		});
		
		/*---------------------------------------------------------------------
			Placeholdem  
		-----------------------------------------------------------------------*/
		
		Placeholdem( document.querySelectorAll( '[placeholder]' ) );
		
		/*---------------------------------------------------------------------
			Image-scroll 
		-----------------------------------------------------------------------*/
		
		if ($('.screen').length) {
			$(window).on('load', function() {
				$( '.screen' ).scrollImage();   
			 });
			}
			
		/*---------------------------------------------------------------------
			Particles-js
		-----------------------------------------------------------------------*/
		
		particlesJS("particles-js", {
		  "particles": {
			"number": {
			  "value": 80,
			  "density": {
				"enable": true,
				"value_area": 800
			  }
			},
			"color": {
			  "value": "#ffffff"
			},
			"shape": {
			  "type": "circle",
			  "stroke": {
				"width": 0,
				"color": "#000000"
			  },
			  "polygon": {
				"nb_sides": 5
			  },
			  "image": {
				"src": "img/github.svg",
				"width": 100,
				"height": 100
			  }
			},
			"opacity": {
			  "value": 0.5,
			  "random": false,
			  "anim": {
				"enable": false,
				"speed": 1,
				"opacity_min": 0.1,
				"sync": false
			  }
			},
			"size": {
			  "value": 2,
			  "random": true,
			  "anim": {
				"enable": false,
				"speed": 40,
				"size_min": 0.1,
				"sync": false
			  }
			},
			"line_linked": {
			  "enable": true,
			  "distance": 150,
			  "color": "#ffffff",
			  "opacity": 0.4,
			  "width": 1
			},
			"move": {
			  "enable": true,
			  "speed": 2,
			  "direction": "none",
			  "random": false,
			  "straight": false,
			  "out_mode": "out",
			  "bounce": false,
			  "attract": {
				"enable": false,
				"rotateX": 600,
				"rotateY": 1200
			  }
			}
		  },
		  "interactivity": {
			"detect_on": "canvas",
			"events": {
			  "onhover": {
				"enable": true,
				"mode": "grab"
			  },
			  "onclick": {
				"enable": true,
				"mode": "push"
			  },
			  "resize": true
			},
			"modes": {
			  "grab": {
				"distance": 150,
				"line_linked": {
				  "opacity": 1
				}
			  },
			  "bubble": {
				"distance": 400,
				"size": 40,
				"duration": 2,
				"opacity": 8,
				"speed": 3
			  },
			  "repulse": {
				"distance": 200,
				"duration": 0.4
			  },
			  "push": {
				"particles_nb": 4
			  },
			  "remove": {
				"particles_nb": 2
			  }
			}
		  },
		  "retina_detect": true
		});

		requestAnimationFrame();
		
		
})(jQuery);
