// =========================================
// LegalDecode - Website JavaScript
// =========================================

document.addEventListener("DOMContentLoaded", function () {

    // Mobile menu
    const menuToggle = document.getElementById("menuToggle");
    const navMenu = document.getElementById("navMenu");

    if (menuToggle && navMenu) {

        menuToggle.addEventListener("click", function () {
            navMenu.classList.toggle("active");
        });

        // Close menu after clicking a navigation link
        const navLinks = navMenu.querySelectorAll("a");

        navLinks.forEach(function (link) {

            link.addEventListener("click", function () {
                navMenu.classList.remove("active");
            });

        });
    }


    // Contact form
    const contactForm = document.getElementById("contactForm");

    if (contactForm) {

        contactForm.addEventListener("submit", function (event) {

            event.preventDefault();

            const name = document.getElementById("name").value.trim();
            const phone = document.getElementById("phone").value.trim();
            const email = document.getElementById("email").value.trim();
            const message = document.getElementById("message").value.trim();

            if (!name || !phone || !message) {

                alert("Please enter your name, phone number and brief description of your legal matter.");

                return;
            }

            /*
             * अभी form केवल basic validation करता है।
             * बाद में इसे WhatsApp या Email से connect करेंगे।
             */

            const whatsappNumber = "919999999999";

            const whatsappMessage =
                "Legal Consultation Request%0A%0A" +
                "Name: " + encodeURIComponent(name) + "%0A" +
                "Phone: " + encodeURIComponent(phone) + "%0A" +
                "Email: " + encodeURIComponent(email) + "%0A" +
                "Legal Matter: " + encodeURIComponent(message);

            const whatsappURL =
                "https://wa.me/" +
                whatsappNumber +
                "?text=" +
                whatsappMessage;

            const openWhatsApp = confirm(
                "Your details are ready. Do you want to send your consultation request on WhatsApp?"
            );

            if (openWhatsApp) {
                window.open(whatsappURL, "_blank");
            }

        });
    }


    // Current year in footer
    const yearElements = document.querySelectorAll(".current-year");

    yearElements.forEach(function (element) {
        element.textContent = new Date().getFullYear();
    });

});
