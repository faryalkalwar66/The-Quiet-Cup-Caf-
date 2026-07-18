// server.js
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const path = require('path');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(__dirname));

// MongoDB Connection (Local or Cloud)
const MONGODB_URI = 'mongodb+srv://faryalkalwar66_db_user:2dgNsQli7wfZcIfI@cluster0.fv6bjby.mongodb.net/quietcup?retryWrites=true&w=majority&appName=Cluster0';
mongoose.connect(MONGODB_URI)
.then(() => console.log('✅ Connected to MongoDB (' + (process.env.MONGODB_URI ? 'Cloud Atlas' : 'Local') + ')'))
.catch(err => console.error('❌ MongoDB Connection Error:', err));

// --- Schemas & Models ---
const Reservation = mongoose.model('Reservation', new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true },
    date: { type: String, required: true },
    time: { type: String, required: true },
    guests: { type: Number, required: true },
    notes: { type: String },
    status: { type: String, default: 'Pending' },
    createdAt: { type: Date, default: Date.now }
}));

const Review = mongoose.model('Review', new mongoose.Schema({
    name: { type: String, required: true },
    rating: { type: Number, required: true, min: 1, max: 5 },
    comment: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
}));

const Subscriber = mongoose.model('Subscriber', new mongoose.Schema({
    email: { type: String, required: true, unique: true },
    joinedAt: { type: Date, default: Date.now }
}));

const Order = mongoose.model('Order', new mongoose.Schema({
    customerName: { type: String, required: true },
    items: [{ name: String, price: Number, quantity: Number }],
    totalAmount: { type: Number, required: true },
    status: { type: String, default: 'Pending' },
    createdAt: { type: Date, default: Date.now }
}));

// --- API Routes ---
app.post('/api/reservations', async (req, res) => {
    try {
        const newReservation = new Reservation(req.body);
        await newReservation.save();
        res.status(201).json({ message: 'Reservation successful!', reservation: newReservation });
    } catch (error) {
        res.status(500).json({ error: 'Failed to create reservation' });
    }
});

app.post('/api/reviews', async (req, res) => {
    try {
        const newReview = new Review(req.body);
        await newReview.save();
        res.status(201).json({ message: 'Review added successfully!', review: newReview });
    } catch (error) {
        res.status(500).json({ error: 'Failed to add review' });
    }
});

app.get('/api/reviews', async (req, res) => {
    try {
        const reviews = await Review.find().sort({ createdAt: -1 });
        res.status(200).json(reviews);
    } catch (error) {
        res.status(500).json({ error: 'Failed to fetch reviews' });
    }
});

app.post('/api/subscribe', async (req, res) => {
    try {
        const { email } = req.body;
        const existing = await Subscriber.findOne({ email });
        if (existing) {
            return res.status(400).json({ message: 'Email already subscribed!' });
        }
        const newSubscriber = new Subscriber({ email });
        await newSubscriber.save();
        res.status(201).json({ message: 'Welcome to The Quiet Club!' });
    } catch (error) {
        res.status(500).json({ error: 'Failed to subscribe' });
    }
});

app.post('/api/orders', async (req, res) => {
    try {
        const newOrder = new Order(req.body);
        await newOrder.save();
        res.status(201).json({ message: 'Order placed successfully!', order: newOrder });
    } catch (error) {
        res.status(500).json({ error: 'Failed to place order: ' + error.message });
    }
});

app.listen(PORT, () => {
    console.log('🚀 Server running on http://localhost:' + PORT);
});
