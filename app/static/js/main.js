const btn = document.getElementById("scrollTop");

if (btn) {

    window.addEventListener("scroll", () => {

        if (document.documentElement.scrollTop > 300) {

            btn.style.display = "block";

        } else {

            btn.style.display = "none";

        }

    });

    btn.addEventListener("click", () => {

        window.scrollTo({

            top: 0,

            behavior: "smooth"

        });

    });

}