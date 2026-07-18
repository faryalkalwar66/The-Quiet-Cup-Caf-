import re

menu_data = [
    ("hot-classics", "Hot Classics", [
        ("Espresso", "3.00", "espresso-quiet-cup-cafe.jpg"),
        ("Double Espresso", "4.00", "espresso-quiet-cup-cafe.jpg"),
        ("Americano", "3.50", "americano-quiet-cup-cafe.jpg"),
        ("Cappuccino", "4.00", "cappuccino-quiet-cup-cafe.webp"),
        ("Latte", "4.00", "latte-quiet-cup-cafe.avif"),
        ("Flat White", "4.20", "latte-quiet-cup-cafe.avif"),
        ("Macchiato", "3.80", "macchiato-quiet-cup-cafe.jpeg"),
        ("Cortado", "3.70", "cortado-quiet-cup-cafe.jpg")
    ]),
    ("cold-brews", "Cold Brews & Frappes", [
        ("Cold Brew", "4.00", "cold-brew-quiet-cup-cafe.jpg"),
        ("Nitro Cold Brew", "4.50", "cold-brew-quiet-cup-cafe.jpg"),
        ("Iced Latte", "4.20", "latte-quiet-cup-cafe.avif"),
        ("Iced Americano", "3.80", "americano-quiet-cup-cafe.jpg"),
        ("Caramel Frappe", "5.50", "frappe-placeholder.jpg"),
        ("Mocha Frappe", "5.50", "frappe-placeholder.jpg"),
        ("Vanilla Frappe", "5.00", "frappe-placeholder.jpg"),
        ("Matcha Frappe", "5.80", "frappe-placeholder.jpg")
    ]),
    ("signatures", "Signatures", [
        ("Turkish Coffee", "4.00", "turkish-coffee-quiet-cup-cafe.jpg"),
        ("Irish Coffee", "5.00", "irish-coffee-quiet-cup-cafe.jpg"),
        ("Affogato", "4.50", "affogato-quiet-cup-cafe.jpg"),
        ("Mocha", "4.50", "mocha-quiet-cup-cafe.jpg"),
        ("White Chocolate Mocha", "4.80", "mocha-quiet-cup-cafe.jpg"),
        ("Caramel Macchiato", "4.50", "macchiato-quiet-cup-cafe.jpeg"),
        ("Honey Lavender Latte", "5.20", "latte-quiet-cup-cafe.avif")
    ]),
    ("teas", "Teas & Infusions", [
        ("Classic Chai", "3.50", "tea-placeholder.jpg"),
        ("Matcha Latte", "4.80", "tea-placeholder.jpg"),
        ("Earl Grey", "3.00", "tea-placeholder.jpg"),
        ("Chamomile Herbal", "3.00", "tea-placeholder.jpg"),
        ("Peppermint Tea", "3.00", "tea-placeholder.jpg"),
        ("Iced Peach Tea", "3.80", "tea-placeholder.jpg")
    ]),
    ("bakery", "Bakery & Pastries", [
        ("Butter Croissant", "3.50", "pastry-placeholder.jpg"),
        ("Chocolate Croissant", "4.00", "pastry-placeholder.jpg"),
        ("Almond Croissant", "4.20", "pastry-placeholder.jpg"),
        ("Blueberry Muffin", "3.50", "pastry-placeholder.jpg"),
        ("Banana Nut Muffin", "3.50", "pastry-placeholder.jpg"),
        ("Everything Bagel", "4.00", "pastry-placeholder.jpg")
    ]),
    ("desserts", "Desserts", [
        ("NY Cheesecake", "5.50", "dessert-placeholder.jpg"),
        ("Fudge Brownie", "4.00", "dessert-placeholder.jpg"),
        ("Tiramisu", "6.00", "dessert-placeholder.jpg"),
        ("Lemon Tart", "4.50", "dessert-placeholder.jpg"),
        ("Red Velvet Cake", "5.50", "dessert-placeholder.jpg")
    ])
]

html_blocks = []
html_blocks.append('<div class="menu-items-grid">')

for cat_id, cat_name, items in menu_data:
    html_blocks.append(f'\\n    <h2 id="{cat_id}" class="menu-category-title animate-in" style="grid-column: 1 / -1; margin-top: 40px;">{cat_name}</h2>\\n')
    for name, price, img in items:
        html_blocks.append(f'''    <div class="menu-item animate-in" data-name="{name}" data-price="{price}">
        <img src="assets/{img}" alt="{name}">
        <h3>{name}</h3>
        <p></p>
        <button class="add-to-cart-btn">Add to Cart</button>
    </div>''')

html_blocks.append('</div>')
new_menu_html = "\\n".join(html_blocks)

with open('menu.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the content inside <section class="menu-items-section">
new_content = re.sub(r'<div class="menu-items-grid">.*?</div>\\s*</section>', new_menu_html + '\\n            </section>', content, flags=re.DOTALL)

with open('menu.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
