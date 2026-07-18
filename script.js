// Mobile navigation toggle
var menuToggle = document.querySelector('.menu-toggle');
var navLinks = document.querySelector('.nav-links');

if (menuToggle && navLinks) {
    menuToggle.addEventListener('click', function () {
        var isOpen = navLinks.classList.toggle('open');
        menuToggle.setAttribute('aria-expanded', isOpen);
    });

    // Close menu after a link is tapped (mobile)
    navLinks.querySelectorAll('a').forEach(function (link) {
        link.addEventListener('click', function () {
            navLinks.classList.remove('open');
            menuToggle.setAttribute('aria-expanded', false);
        });
    });
}

// Contact form handling (only present on contact.html)
var contactForm = document.querySelector('.contact-form');

if (contactForm) {
    contactForm.addEventListener('submit', function (event) {
        event.preventDefault();

        var status = document.querySelector('.form-status');
        if (status) {
            status.textContent = "Thank you for contacting The Quiet Cup Café! ☕ We'll get back to you soon.";
        } else {
            alert("Thank you for contacting The Quiet Cup Café! ☕ We'll get back to you soon.");
        }

        contactForm.reset();
    });
}

/* ============================================================
   Dark Mode Toggle
============================================================ */
(function () {
    var themeToggle = document.getElementById('themeToggle');
    var body = document.body;
    var savedTheme = localStorage.getItem('quietcup-theme');

    if (savedTheme === 'dark') {
        body.classList.add('dark-mode');
        if (themeToggle) themeToggle.textContent = '☀️';
    }

    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            var isDark = body.classList.toggle('dark-mode');
            themeToggle.textContent = isDark ? '☀️' : '🌙';
            localStorage.setItem('quietcup-theme', isDark ? 'dark' : 'light');
        });
    }
})();

/* ============================================================
   Toast helper
============================================================ */
function showToast(message) {
    var toast = document.getElementById('toast');
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add('show');
    clearTimeout(showToast._t);
    showToast._t = setTimeout(function () {
        toast.classList.remove('show');
    }, 2500);
}

/* ============================================================
   Cart / Ordering system
============================================================ */
(function () {
    var CART_KEY = 'quietcup-cart';

    function getCart() {
        try {
            return JSON.parse(localStorage.getItem(CART_KEY)) || [];
        } catch (e) {
            return [];
        }
    }

    function saveCart(cart) {
        localStorage.setItem(CART_KEY, JSON.stringify(cart));
    }

    function updateCartCount() {
        var cart = getCart();
        var count = cart.reduce(function (sum, item) { return sum + item.qty; }, 0);
        var countEl = document.getElementById('cartCount');
        if (countEl) countEl.textContent = count;
    }

    function renderCart() {
        var cart = getCart();
        var itemsEl = document.getElementById('cartItems');
        var totalEl = document.getElementById('cartTotal');
        if (!itemsEl) return;

        itemsEl.innerHTML = '';

        if (cart.length === 0) {
            itemsEl.innerHTML = '<p class="cart-empty">Your cart is empty.</p>';
        } else {
            cart.forEach(function (item, index) {
                var row = document.createElement('div');
                row.className = 'cart-item';
                row.innerHTML =
                    '<div class="cart-item-info">' +
                        '<p class="cart-item-name">' + item.name + '</p>' +
                        '<p class="cart-item-price">$' + item.price.toFixed(2) + '</p>' +
                    '</div>' +
                    '<div class="cart-item-controls">' +
                        '<button class="qty-btn" data-action="dec" data-index="' + index + '">-</button>' +
                        '<span class="qty-value">' + item.qty + '</span>' +
                        '<button class="qty-btn" data-action="inc" data-index="' + index + '">+</button>' +
                        '<button class="remove-btn" data-index="' + index + '" title="Remove">🗑</button>' +
                    '</div>';
                itemsEl.appendChild(row);
            });
        }

        var total = cart.reduce(function (sum, item) { return sum + item.qty * item.price; }, 0);
        if (totalEl) totalEl.textContent = '$' + total.toFixed(2);

        updateCartCount();
    }

    function addToCart(name, price) {
        var cart = getCart();
        var existing = cart.filter(function (i) { return i.name === name; })[0];
        if (existing) {
            existing.qty += 1;
        } else {
            cart.push({ name: name, price: price, qty: 1 });
        }
        saveCart(cart);
        renderCart();
        showToast(name + ' added to cart ☕');
    }

    document.querySelectorAll('.add-to-cart-btn').forEach(function (btn) {
        btn.addEventListener('click', function () {
            var item = btn.closest('.menu-item');
            if (!item) return;
            var name = item.getAttribute('data-name');
            var price = parseFloat(item.getAttribute('data-price'));
            addToCart(name, price);
        });
    });

    document.addEventListener('click', function (e) {
        if (e.target.classList.contains('qty-btn')) {
            var index = parseInt(e.target.getAttribute('data-index'), 10);
            var action = e.target.getAttribute('data-action');
            var cart = getCart();
            if (!cart[index]) return;
            if (action === 'inc') cart[index].qty += 1;
            if (action === 'dec') {
                cart[index].qty -= 1;
                if (cart[index].qty <= 0) cart.splice(index, 1);
            }
            saveCart(cart);
            renderCart();
        }
        if (e.target.classList.contains('remove-btn')) {
            var idx = parseInt(e.target.getAttribute('data-index'), 10);
            var cart2 = getCart();
            cart2.splice(idx, 1);
            saveCart(cart2);
            renderCart();
        }
    });

    var cartToggle = document.getElementById('cartToggle');
    var cartDrawer = document.getElementById('cartDrawer');
    var cartOverlay = document.getElementById('cartOverlay');
    var cartClose = document.getElementById('cartClose');

    function openCart() {
        if (cartDrawer) cartDrawer.classList.add('open');
        if (cartOverlay) cartOverlay.classList.add('show');
    }

    function closeCart() {
        if (cartDrawer) cartDrawer.classList.remove('open');
        if (cartOverlay) cartOverlay.classList.remove('show');
    }

    if (cartToggle) cartToggle.addEventListener('click', openCart);
    if (cartClose) cartClose.addEventListener('click', closeCart);
    if (cartOverlay) cartOverlay.addEventListener('click', closeCart);

    // Backend integration handles placeOrderBtn click now
    // Dummy cart logic removed

    renderCart();
})();

/* ============================================================
   Reviews submission
============================================================ */
(function () {
    var REVIEWS_KEY = 'quietcup-reviews';
    var starRating = document.getElementById('starRating');
    var reviewForm = document.getElementById('reviewForm');
    var reviewsContainer = document.querySelector('.reviews-container');

    if (!reviewForm || !reviewsContainer) return;

    var selectedStars = 0;
    var stars = starRating ? starRating.querySelectorAll('span') : [];

    function highlightStars(count) {
        stars.forEach(function (star, i) {
            star.classList.toggle('selected', i < count);
        });
    }

    stars.forEach(function (star) {
        star.addEventListener('click', function () {
            selectedStars = parseInt(star.getAttribute('data-value'), 10);
            highlightStars(selectedStars);
        });
        star.addEventListener('mouseover', function () {
            highlightStars(parseInt(star.getAttribute('data-value'), 10));
        });
    });

    if (starRating) {
        starRating.addEventListener('mouseleave', function () {
            highlightStars(selectedStars);
        });
    }

    function getStoredReviews() {
        try {
            return JSON.parse(localStorage.getItem(REVIEWS_KEY)) || [];
        } catch (e) {
            return [];
        }
    }

    function addReviewCard(review, animate) {
        var card = document.createElement('div');
        card.className = 'review-card' + (animate ? ' new-review' : '');
        card.innerHTML =
            '<p class="review-text">"' + review.text + '"</p>' +
            '<div class="review-stars">' + '⭐'.repeat(review.stars) + '</div>' +
            '<p class="review-author">- ' + review.name + '</p>';
        reviewsContainer.prepend(card);
    }

    function renderStoredReviews() {
        var reviews = getStoredReviews();
        // reverse so the most recently added still ends up on top after each prepend
        reviews.slice().reverse().forEach(function (review) {
            addReviewCard(review, false);
        });
    }

    reviewForm.addEventListener('submit', async function (e) {
        e.preventDefault();
        var nameInput = document.getElementById('reviewName');
        var textInput = document.getElementById('reviewText');
        var status = document.getElementById('reviewStatus');

        if (selectedStars === 0) {
            if (status) status.textContent = 'Please select a star rating.';
            return;
        }

        const payload = {
            name: nameInput.value.trim(),
            text: textInput.value.trim(),
            rating: selectedStars,
            comment: textInput.value.trim() // MongoDB expects 'comment'
        };

        try {
            const API_URL = 'http://localhost:3000/api';
            const res = await fetch(`${API_URL}/reviews`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            if(res.ok) {
                if (status) status.textContent = 'Thank you for your review! ☕ Saved to Database.';
                reviewForm.reset();
                selectedStars = 0;
                highlightStars(0);
                
                // Add dynamically to UI
                var reviewUI = { name: payload.name, text: payload.comment, stars: payload.rating };
                var reviews = getStoredReviews();
                reviews.unshift(reviewUI);
                localStorage.setItem(REVIEWS_KEY, JSON.stringify(reviews));
                addReviewCard(reviewUI, true);
            }
        } catch (error) {
            if (status) status.textContent = 'Failed to connect to server.';
        }
    });

    renderStoredReviews();
})();

/* ============================================================
   Reservations Dummy Code Removed (Handled by Backend)
============================================================ */

/* ============================================================
   Scroll Animations (Intersection Observer)
============================================================ */
(function () {
    var animatedElements = document.querySelectorAll('.feature-card, .popular-card, .menu-item, .about-image, .about-details');

    if ('IntersectionObserver' in window) {
        var observer = new IntersectionObserver(function(entries, obs) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                    obs.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1, rootMargin: "0px 0px -50px 0px" });

        animatedElements.forEach(function(el) {
            observer.observe(el);
        });
    } else {
        // Fallback for older browsers
        animatedElements.forEach(function(el) {
            el.classList.add('animate-in');
        });
    }
})();
/* =========================================
   NEW WOW-FACTOR FEATURES (Cursor & Preloader)
   ========================================= */

// 1. Preloader Fade Out
window.addEventListener('load', () => {
    const preloader = document.getElementById('preloader');
    if (preloader) {
        setTimeout(() => {
            preloader.classList.add('hidden');
        }, 500); // Small delay for effect
    }
});

// 2. Custom Magic Cursor (Disabled by User request)

// 3. Initialize AOS (Animate On Scroll) robustly
window.addEventListener('load', () => {
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-out-cubic',
            once: true,
            offset: 50
        });
    } else {
        // Fallback if CDN fails: reveal everything
        document.querySelectorAll('[data-aos]').forEach(el => {
            el.style.opacity = '1';
            el.style.transform = 'none';
        });
    }
});

// ==========================================
// BACKEND INTEGRATION (Node.js + MongoDB)
// ==========================================
const API_URL = '/api';

// 1. The Quiet Club (Footer Newsletter)
document.querySelectorAll('.club-form').forEach(form => {
    form.onsubmit = async (e) => {
        e.preventDefault();
        const emailInput = form.querySelector('input[type="email"]');
        const btn = form.querySelector('button');
        const originalText = btn.innerText;
        btn.innerText = 'Joining...';
        
        try {
            const res = await fetch(`${API_URL}/subscribe`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email: emailInput.value })
            });
            const data = await res.json();
            alert(data.message);
            if(res.ok) emailInput.value = '';
        } catch (error) {
            alert('Failed to connect to server.');
        } finally {
            btn.innerText = originalText;
        }
    };
});

// 2. Reservations
const resForm = document.getElementById('reservationForm');
if (resForm) {
    resForm.onsubmit = async (e) => {
        e.preventDefault();
        const btn = resForm.querySelector('button');
        const status = document.getElementById('reservationStatus');
        btn.innerText = 'Reserving...';
        
        const payload = {
            name: document.getElementById('resName').value,
            email: document.getElementById('resEmail').value,
            date: document.getElementById('resDate').value,
            time: document.getElementById('resTime').value,
            guests: document.getElementById('resGuests').value,
            notes: document.getElementById('resNotes').value
        };

        try {
            const res = await fetch(`${API_URL}/reservations`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const data = await res.json();
            status.style.color = res.ok ? 'var(--accent-color)' : 'red';
            status.innerText = data.message || data.error;
            if(res.ok) resForm.reset();
        } catch (error) {
            status.style.color = 'red';
            status.innerText = 'Failed to connect to server.';
        } finally {
            btn.innerText = 'Reserve Table';
        }
    };
}

// 3. Cart Checkout (Orders)
const placeOrderBtnBackend = document.getElementById('placeOrderBtn');
if (placeOrderBtnBackend) {
    placeOrderBtnBackend.onclick = async () => {
        let cart = [];
        try { cart = JSON.parse(localStorage.getItem('quietcup-cart')) || []; } catch(e){}
        
        if (cart.length === 0) return alert('Your cart is empty!');
        
        const customerName = prompt('Please enter your name for the order:');
        if (!customerName) return;

        placeOrderBtnBackend.innerText = 'Placing Order...';
        
        const totalAmount = cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
        const payload = { customerName, items: cart, totalAmount };

        try {
            const res = await fetch(`${API_URL}/orders`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const data = await res.json();
            alert(data.message || data.error);
            if(res.ok) {
                localStorage.setItem('quietcup-cart', JSON.stringify([]));
                location.reload(); // Reload to refresh UI instantly
            }
        } catch (error) {
            alert('Failed to place order. Server offline.');
        } finally {
            placeOrderBtnBackend.innerText = 'Place Order';
        }
    };
}
