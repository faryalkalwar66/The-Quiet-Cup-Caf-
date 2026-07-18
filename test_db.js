const mongoose = require('mongoose');

mongoose.connect('mongodb://127.0.0.1:27017/quietcup').then(async () => {
    const Order = mongoose.model('Order', new mongoose.Schema({}, { strict: false }));
    const count = await Order.countDocuments();
    const orders = await Order.find();
    console.log(Order count: );
    console.log(orders);
    process.exit(0);
}).catch(console.error);
