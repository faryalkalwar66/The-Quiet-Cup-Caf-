from fpdf import FPDF
import os

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", 'B', 24)
pdf.cell(0, 20, "The Quiet Cup Cafe - Menu", ln=True, align='C')
pdf.ln(10)

menu = [
    ("Hot Classics", [
        ("Espresso", ".00", "espresso-quiet-cup-cafe.jpg"),
        ("Americano", ".50", "americano-quiet-cup-cafe.jpg"),
    ]),
    ("Signatures", [
        ("Turkish Coffee", ".00", "turkish-coffee-quiet-cup-cafe.jpg"),
        ("Irish Coffee", ".00", "irish-coffee-quiet-cup-cafe.jpg"),
        ("Affogato", ".50", "affogato-quiet-cup-cafe.jpg"),
    ]),
    ("Cold Brews & Extras", [
        ("Cold Brew", ".00", "cold-brew-quiet-cup-cafe.jpg"),
        ("Mocha", ".50", "mocha-quiet-cup-cafe.jpg"),
        ("Macchiato", ".80", "macchiato-quiet-cup-cafe.jpeg"),
        ("Cortado", ".70", "cortado-quiet-cup-cafe.jpg"),
    ])
]

for category, items in menu:
    pdf.set_font("Arial", 'B', 18)
    pdf.cell(0, 15, category, ln=True)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)
    
    for name, price, img in items:
        y_before = pdf.get_y()
        if y_before > 250:
            pdf.add_page()
            y_before = pdf.get_y()
            
        img_path = f"assets/{img}"
        if os.path.exists(img_path):
            try:
                pdf.image(img_path, x=15, y=y_before, w=25, h=25)
            except Exception as e:
                pass
        
        pdf.set_xy(45, y_before + 5)
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(100, 10, name)
        
        pdf.set_font("Arial", '', 14)
        pdf.cell(40, 10, price, ln=True, align='R')
        
        pdf.set_y(y_before + 30)

pdf.output("assets/CoffeeShop-Menu.pdf")
