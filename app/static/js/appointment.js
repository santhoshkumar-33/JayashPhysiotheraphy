/*==========================================
    JAYASH PHYSIO
    Appointment Page
==========================================*/

document.addEventListener("DOMContentLoaded", () => {

    //---------------------------------------
    // Character Counter
    //---------------------------------------

    const problemField = document.querySelector(
        'textarea[name="problem"]'
    );

    const counter = document.getElementById("char-count");

    if (problemField && counter) {

        const updateCounter = () => {

            const length = problemField.value.length;

            counter.textContent = `${length} / 500`;

            if (length > 450) {

                counter.classList.add("text-danger");

            } else {

                counter.classList.remove("text-danger");

            }

        };

        updateCounter();

        problemField.addEventListener("input", updateCounter);

    }

    //---------------------------------------
    // Disable Past Dates
    //---------------------------------------

    const dateInput = document.querySelector(
        'input[name="preferred_date"]'
    );

    if (dateInput) {

        const today = new Date().toISOString().split("T")[0];

        dateInput.min = today;

    }

    //---------------------------------------
    // Loading Button
    //---------------------------------------

    const form = document.querySelector("form");

    const submitBtn = document.querySelector(
        'input[type="submit"]'
    );

    if (form && submitBtn) {

        form.addEventListener("submit", function () {

            if (form.checkValidity()) {

                submitBtn.disabled = true;

                submitBtn.value = "Redirecting to WhatsApp...";

            }

        });

    }

});