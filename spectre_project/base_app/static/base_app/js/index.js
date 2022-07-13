function teamSlider() {
    var swiper = new Swiper('.team .swiper-container', {
        slidesPerView: 2,
        spaceBetween: 50,
        speed: 1000,
        loop: true,
        navigation: {
            nextEl: '.team .swiper-button-next',
            prevEl: '.team .swiper-button-prev',
        },
        pagination: {
            el: '.team .swiper-pagination',
            type: 'bullets',
            clickable: true,
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                spaceBetween: 0,

            },
            992: {
                slidesPerView: 1,
            },
            1200: {
                slidesPerView: 2,
                spaceBetween: 50
            }
        }
    });
}

function whySlider() {
    var swiper = new Swiper('.why .swiper-container', {
        slidesPerView: 2,
        spaceBetween: 30,
        speed: 1000,
        loop: true,
        pagination: {
            el: '.why .swiper-pagination',
            type: 'bullets',
            clickable: true,
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                spaceBetween: 30,

            },
            768: {
                slidesPerView: 2,
            },
            1200: {
                slidesPerView: 2,
                spaceBetween: 10
            }
        }
    });
}


$(document).ready(function() {
    teamSlider()
    if ($(window).innerWidth() < 992) {
        whySlider()
    }


    $(".offer__tab").click(function() {
        let path = $(this).attr("data-tab-path")
        $(".offer__tab").removeClass("offer__tab--active")
        $(this).addClass("offer__tab--active")
        $(`.offer__content`).removeClass("offer__content--active")
        $(`.offer__content[data-content-path='${path}']`).addClass("offer__content--active")
    })

    $(".our-work__item-show").click(function() {
        if ($(this).hasClass('our-work__item-show--active')) {
            $(this).removeClass("our-work__item-show--active")
        } else {
            $(".our-work__item-show").removeClass("our-work__item-show--active")
            $(this).addClass("our-work__item-show--active")
        }

    })

    $(".header__burger").click(function() {
        $(this).toggleClass("header__burger--active")
        $(".header__right").slideToggle()
    })

    $(".nav-dropdown-show").click(function() {
        $(this).addClass("nav-dropdown-show--active")
    })

    $(document).mouseup(function(e) { // событие клика по веб-документу
        var div = $(".nav-dropdown-hidden"); // тут указываем ID элемента
        if (!div.is(e.target) // если клик был не по нашему блоку
            &&
            div.has(e.target).length === 0 &&
            $(".nav-dropdown-show").hasClass("nav-dropdown-show--active")) { // и не по его дочерним элементам
            $(".nav-dropdown-show").removeClass("nav-dropdown-show--active")
        }
    });
})