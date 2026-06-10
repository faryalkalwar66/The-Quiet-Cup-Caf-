var navLinks = document.querySelectorAll('.nav-links a');

for (var i = 0; i < navLinks.length; i++) {
    navLinks[i].addEventListener('click', function (event) {
        event.preventDefault();

        var sectionName = this.innerText.toLowerCase();
        var targetSection = document.querySelector('.' + sectionName + '-section');

        if (targetSection) {
            targetSection.scrollIntoView({ behavior: 'smooth' });
        }
    });
}

var contactForm = document.querySelector('.contact-form');

contactForm.addEventListener('submit', function (event) {
    event.preventDefault();

    alert("Thank you for contacting The Quiet Cup Café! ☕ We’ll get back to you soon.");

    contactForm.reset();
});