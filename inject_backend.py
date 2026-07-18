import re

backend_js = '''
// ==========================================
// BACKEND INTEGRATION (Node.js + MongoDB)
// ==========================================
const API_URL = 'http://localhost:3000/api';

// 1. The Quiet Club (Footer Newsletter)
document.querySelectorAll('.club-form').forEach(form => {
    form.onsubmit = async (e) => {
        e.preventDefault();
        const emailInput = form.querySelector('input[type="email"]');
        const btn = form.querySelector('button');
        const originalText = btn.innerText;
        btn.innerText = 'Joining...';
        
        try {
            const res = await fetch(${API_URL}/subscribe, {
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
            const res = await fetch(${API_URL}/reservations, {
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
const placeOrderBtn = document.getElementById('placeOrderBtn');
if (placeOrderBtn) {
    placeOrderBtn.onclick = async () => {
        if (cart.length === 0) return alert('Your cart is empty!');
        
        const customerName = prompt('Please enter your name for the order:');
        if (!customerName) return;

        placeOrderBtn.innerText = 'Placing Order...';
        
        const totalAmount = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
        const payload = { customerName, items: cart, totalAmount };

        try {
            const res = await fetch(${API_URL}/orders, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const data = await res.json();
            alert(data.message || data.error);
            if(res.ok) {
                cart = [];
                updateCartUI();
                document.getElementById('cartDrawer').classList.remove('open');
                document.getElementById('cartOverlay').classList.remove('active');
            }
        } catch (error) {
            alert('Failed to place order. Server offline.');
        } finally {
            placeOrderBtn.innerText = 'Place Order';
        }
    };
}
'''

with open('script.js', 'a', encoding='utf-8') as f:
    f.write(backend_js)

print("Backend JS integration complete.")
