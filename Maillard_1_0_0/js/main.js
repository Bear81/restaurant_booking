/* ===================================================================
 * Maillard 1.0.0 - Main JS
 *
 * ------------------------------------------------------------------- */

(function(html) {

    'use strict';


   /* preloader
    * -------------------------------------------------- */
    const ssPreloader = function() {

        const siteBody = document.querySelector('body');
        const preloader = document.querySelector('#preloader');
        if (!preloader) return;

        html.classList.add('ss-preload');
        
        window.addEventListener('load', function() {
            html.classList.remove('ss-preload');
            html.classList.add('ss-loaded');
            
            preloader.addEventListener('transitionend', function afterTransition(e) {
                if (e.target.matches('#preloader'))  {
                    siteBody.classList.add('ss-show');
                    e.target.style.display = 'none';
                    preloader.removeEventListener(e.type, afterTransition);
                }
            });
        });

    }; // end ssPreloader


   /* offcanvas nav menu
    * ------------------------------------------------------ */
    const ssOffCanvas = function() {

        const menuToggle  = document.querySelector('.s-header__menu-toggle');
        const nav         = document.querySelector('.s-header__nav');
        const closeButton = document.querySelector('.s-header__nav-close-btn');
        const siteBody    = document.querySelector('body');

        if (!(menuToggle && nav)) return;

        menuToggle.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            siteBody.classList.add('menu-is-open');
        });

        closeButton.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();

            if (siteBody.classList.contains('menu-is-open')) {
                siteBody.classList.remove('menu-is-open');
            }
        });

        siteBody.addEventListener('click', function(e) {
            if(!(e.target.matches('.s-header__nav, .s-header__nav-links a'))) {
                closeButton.dispatchEvent(new Event('click'));
            }
        });

    }; // end ssOffcanvas   


   /* glightbox
    * ------------------------------------------------------ */ 
    const ssGLightbox = function() {

        const lightbox = GLightbox({
            selector: '.glightbox',
            zoomable: false,
            touchNavigation: true,
            loop: false,
            autoplayVideos: true,
            svg: {
                close: '<svg clip-rule="evenodd" fill-rule="evenodd" stroke-linejoin="round" stroke-miterlimit="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="m12 10.93 5.719-5.72c.146-.146.339-.219.531-.219.404 0 .75.324.75.749 0 .193-.073.385-.219.532l-5.72 5.719 5.719 5.719c.147.147.22.339.22.531 0 .427-.349.75-.75.75-.192 0-.385-.073-.531-.219l-5.719-5.719-5.719 5.719c-.146.146-.339.219-.531.219-.401 0-.75-.323-.75-.75 0-.192.073-.384.22-.531l5.719-5.719-5.72-5.719c-.146-.147-.219-.339-.219-.532 0-.425.346-.749.75-.749.192 0 .385.073.531.219z"/></svg>',
                prev: '<svg clip-rule="evenodd" fill-rule="evenodd" stroke-linejoin="round" stroke-miterlimit="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="m9.474 5.209s-4.501 4.505-6.254 6.259c-.147.146-.22.338-.22.53s.073.384.22.53c1.752 1.754 6.252 6.257 6.252 6.257.145.145.336.217.527.217.191-.001.383-.074.53-.221.293-.293.294-.766.004-1.057l-4.976-4.976h14.692c.414 0 .75-.336.75-.75s-.336-.75-.75-.75h-14.692l4.978-4.979c.289-.289.287-.761-.006-1.054-.147-.147-.339-.221-.53-.221-.191-.001-.38.071-.525.215z" fill-rule="nonzero"/></svg>',
                next: '<svg clip-rule="evenodd" fill-rule="evenodd" stroke-linejoin="round" stroke-miterlimit="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="m14.523 18.787s4.501-4.505 6.255-6.26c.146-.146.219-.338.219-.53s-.073-.383-.219-.53c-1.753-1.754-6.255-6.258-6.255-6.258-.144-.145-.334-.217-.524-.217-.193 0-.385.074-.532.221-.293.292-.295.766-.004 1.056l4.978 4.978h-14.692c-.414 0-.75.336-.75.75s.336.75.75.75h14.692l-4.979 4.979c-.289.289-.286.762.006 1.054.148.148.341.222.533.222.19 0 .378-.072.522-.215z" fill-rule="nonzero"/></svg>'
            }
        });        

    } // end ssGLightbox


   /* swiper
    * ------------------------------------------------------ */ 
    const ssSwiper = function() {
        
        const specialtiesSlider = function() {

            const prevButton = document.querySelector('.menublock-btn-prev');
            const nextButton = document.querySelector('.menublock-btn-next');
            const mSlider = document.querySelector('.s-menublock__slider');            
            if (!(mSlider)) return;

            const slider = new Swiper(mSlider, {

                slidesPerView: 1,
                pagination: {
                    // el: '.swiper-pagination',
                    clickable: true,
                    navigation: {
                        nextEl: '.menublock-btn-next',
                        prevEl: '.menublock-btn-prev',
                    }
                },
                breakpoints: {
                    // when window width is > 400px
                    401: {
                        slidesPerView: 1,
                        spaceBetween: 20
                    },
                    // when window width is > 680px
                    681: {
                        slidesPerView: 2,
                        spaceBetween: 44
                    },
                    // when window width is > 1100px
                    1101: {
                        slidesPerView: 3,
                        spaceBetween: 50
                    },
                    // when window width is > 1400px
                    1401: {
                        slidesPerView: 3,
                        spaceBetween: 60
                    }
                }
            });

            prevButton.addEventListener('click', function() {
                if (slider.activeIndex === 0) {                    
                  // At the beginning of the slider
                  slider.slideTo(slider.slides.length - 1); // Go to the last slide
                } else {
                  slider.slidePrev();
                }
            });
              
            nextButton.addEventListener('click', function() {
                if (slider.activeIndex === slider.slides.length - 1) {
                  // At the end of the slider
                  slider.slideTo(0); // Go to the first slide
                } else {
                  slider.slideNext();
                }
            });

        }; // end specialtiesSlider

        
        const testimonialSlider = function() {

            const tSlider = document.querySelector('.s-testimonials__slider');            
            if (!(tSlider)) return;

            const slider = new Swiper(tSlider, {

                slidesPerView: 1,
                pagination: {
                    el: '.swiper-pagination',
                    clickable: true,
                },
                breakpoints: {
                    // when window width is > 400px
                    401: {
                        slidesPerView: 1,
                        spaceBetween: 20
                    },
                    // when window width is > 900px
                    901: {
                        slidesPerView: 2,
                        spaceBetween: 50
                    },
                    // when window width is > 1200px
                    1201: {
                        slidesPerView: 2,
                        spaceBetween: 80
                    }
                }
            });

        }; // end testimonialSlider

        specialtiesSlider();
        testimonialSlider();

    }; // end ssSwiper


   /* alert boxes
    * ------------------------------------------------------ */
    const ssAlertBoxes = function() {

        const boxes = document.querySelectorAll('.alert-box');
  
        boxes.forEach(function(box){

            box.addEventListener('click', function(e) {
                if (e.target.matches('.alert-box__close')) {
                    e.stopPropagation();
                    e.target.parentElement.classList.add('hideit');

                    setTimeout(function() {
                        box.style.display = 'none';
                    }, 500)
                }
            });
        })

    }; // end ssAlertBoxes


   /* smoothscroll
    * ------------------------------------------------------ */
    const ssMoveTo = function() {

        const easeFunctions = {
            easeInQuad: function (t, b, c, d) {
                t /= d;
                return c * t * t + b;
            },
            easeOutQuad: function (t, b, c, d) {
                t /= d;
                return -c * t* (t - 2) + b;
            },
            easeInOutQuad: function (t, b, c, d) {
                t /= d/2;
                if (t < 1) return c/2*t*t + b;
                t--;
                return -c/2 * (t*(t-2) - 1) + b;
            },
            easeInOutCubic: function (t, b, c, d) {
                t /= d/2;
                if (t < 1) return c/2*t*t*t + b;
                t -= 2;
                return c/2*(t*t*t + 2) + b;
            }
        }

        const triggers = document.querySelectorAll('.smoothscroll');
        
        const moveTo = new MoveTo({
            tolerance: 0,
            duration: 1200,
            easing: 'easeInOutCubic',
            container: window
        }, easeFunctions);

        triggers.forEach(function(trigger) {
            moveTo.registerTrigger(trigger);
        });

    }; // end ssMoveTo


   /* Initialize
    * ------------------------------------------------------ */
    (function ssInit() {

        ssPreloader();
        ssOffCanvas();
        ssGLightbox();
        ssSwiper();
        ssAlertBoxes();
        ssMoveTo();

    })();

})(document.documentElement);