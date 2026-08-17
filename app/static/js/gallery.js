document.addEventListener("DOMContentLoaded", () => {

    // Check whether the gallery exists on the current page
    const gallery = document.querySelector(".gallerySwiper");

    if (!gallery) {
        return;
    }

    // Initialize Swiper
    new Swiper(".gallerySwiper", {

        loop: true,

        speed: 800,

        spaceBetween: 25,

        autoplay: {

            delay: 3000,

            disableOnInteraction: false,

            pauseOnMouseEnter: true

        },

        pagination: {

            el: ".swiper-pagination",

            clickable: true,

        },

        navigation: {

            nextEl: ".swiper-button-next",

            prevEl: ".swiper-button-prev",

        },

        breakpoints: {

            0: {

                slidesPerView: 1

            },

            768: {

                slidesPerView: 2

            },

            1200: {

                slidesPerView: 3

            }

        }

    });

});