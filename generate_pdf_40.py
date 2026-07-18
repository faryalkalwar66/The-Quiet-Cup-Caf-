from fpdf import FPDF
import os

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 24)
pdf.cell(0, 20, "The Quiet Cup Cafe - Menu", ln=True, align='C')
pdf.ln(10)

menu_data = [
    ("Hot Classics", [
        ("Espresso", ".00", "espresso-quiet-cup-cafe.jpg"),
        ("Double Espresso", ".00", "espresso-quiet-cup-cafe.jpg"),
        ("Americano", ".50", "americano-quiet-cup-cafe.jpg"),
        ("Cappuccino", ".00", "cappuccino-quiet-cup-cafe.webp"),
        ("Latte", ".00", "latte-quiet-cup-cafe.avif"),
        ("Flat White", ".20", "latte-quiet-cup-cafe.avif"),
        ("Macchiato", ".80", "macchiato-quiet-cup-cafe.jpeg"),
        ("Cortado", ".70", "cortado-quiet-cup-cafe.jpg")
    ]),
    ("Cold Brews & Frappes", [
        ("Cold Brew", ".00", "cold-brew-quiet-cup-cafe.jpg"),
        ("Nitro Cold Brew", ".50", "cold-brew-quiet-cup-cafe.jpg"),
        ("Iced Latte", ".20", "latte-quiet-cup-cafe.avif"),
        ("Iced Americano", ".80", "americano-quiet-cup-cafe.jpg"),
        ("Caramel Frappe", ".50", "frappe-placeholder.jpg"),
        ("Mocha Frappe", ".50", "frappe-placeholder.jpg"),
        ("Vanilla Frappe", ".00", "frappe-placeholder.jpg"),
        ("Matcha Frappe", ".80", "frappe-placeholder.jpg")
    ]),
    ("Signatures", [
        ("Turkish Coffee", ".00", "turkish-coffee-quiet-cup-cafe.jpg"),
        ("Irish Coffee", ".00", "irish-coffee-quiet-cup-cafe.jpg"),
        ("Affogato", ".50", "affogato-quiet-cup-cafe.jpg"),
        ("Mocha", ".50", "mocha-quiet-cup-cafe.jpg"),
        ("White Choc Mocha", ".80", "mocha-quiet-cup-cafe.jpg"),
        ("Caramel Macchiato", ".50", "macchiato-quiet-cup-cafe.jpeg"),
        ("Lavender Latte", ".20", "latte-quiet-cup-cafe.avif")
    ]),
    ("Teas & Infusions", [
        ("Classic Chai", ".50", "tea-placeholder.jpg"),
        ("Matcha Latte", ".80", "tea-placeholder.jpg"),
        ("Earl Grey", ".00", "tea-placeholder.jpg"),
        ("Chamomile Herbal", ".00", "tea-placeholder.jpg"),
        ("Peppermint Tea", ".00", "tea-placeholder.jpg"),
        ("Iced Peach Tea", ".80", "tea-placeholder.jpg")
    ]),
    ("Bakery & Pastries", [
        ("Butter Croissant", ".50", "pastry-placeholder.jpg"),
        ("Choco Croissant", ".00", "pastry-placeholder.jpg"),
        ("Almond Croissant", ".20", "pastry-placeholder.jpg"),
        ("Blueberry Muffin", ".50", "pastry-placeholder.jpg"),
        ("Banana Nut Muffin", ".50", "pastry-placeholder.jpg"),
        ("Everything Bagel", ".00", "pastry-placeholder.jpg")
    ]),
    ("Desserts", [
        ("NY Cheesecake", ".50", "dessert-placeholder.jpg"),
        ("Fudge Brownie", ".00", "dessert-placeholder.jpg"),
        ("Tiramisu", ".00", "dessert-placeholder.jpg"),
        ("Lemon Tart", ".50", "dessert-placeholder.jpg"),
        ("Red Velvet Cake", ".50", "dessert-placeholder.jpg")
    ])
]

for category, items in menu_data:
    pdf.set_font("Arial", 'B', 18)
    pdf.cell(0, 15, category, ln=True)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)
    
    for name, price, img in items:
        y_before = pdf.get_y()
        if y_before > 260:
            pdf.add_page()
            y_before = pdf.get_y()
            
        img_path = f"assets/{img}"
        if os.path.exists(img_path):
            try:
                pdf.image(img_path, x=15, y=y_before, w=20, h=20)
            except Exception as e:
                pass
        
        pdf.set_xy(40, y_before + 3)
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(100, 10, name)
        
        pdf.set_font("Arial", '', 14)
        pdf.cell(45, 10, price, ln=True, align='R')
        
        pdf.set_y(y_before + 25)
    pdf.ln(5)

pdf.output("assets/CoffeeShop-Menu.pdf")
