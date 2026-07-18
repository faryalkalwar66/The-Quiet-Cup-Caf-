import re

gallery_main = '''
    <main>
        <section class="menu-header">
            <div class="menu-title-wrapper" data-aos="fade-up">
                <h1 class="menu-title">Our Vibe</h1>
                <p style="text-align:center; color: var(--text-light); margin-top: 10px;">A visual journey through The Quiet Cup Cafe.</p>
            </div>
        </section>

        <section class="gallery-section">
            <div class="gallery-masonry">
                <div class="gallery-item large" data-aos="fade-up">
                    <img src="assets/quiet-cup-cafe-interior.jpg" alt="Cafe Interior">
                    <div class="gallery-overlay"><span>The Atmosphere</span></div>
                </div>
                <div class="gallery-item" data-aos="fade-up" data-aos-delay="100">
                    <img src="assets/reservation-table.jpg" alt="Reservation Table">
                    <div class="gallery-overlay"><span>Cozy Corners</span></div>
                </div>
                <div class="gallery-item" data-aos="fade-up" data-aos-delay="200">
                    <img src="assets/espresso-quiet-cup-cafe.jpg" alt="Espresso Shot">
                    <div class="gallery-overlay"><span>The Perfect Pull</span></div>
                </div>
                <div class="gallery-item wide" data-aos="fade-up" data-aos-delay="300">
                    <img src="assets/pastry-placeholder.jpg" alt="Pastries">
                    <div class="gallery-overlay"><span>Fresh Bakery</span></div>
                </div>
                <div class="gallery-item" data-aos="fade-up" data-aos-delay="400">
                    <img src="assets/mocha-quiet-cup-cafe.jpg" alt="Mocha Art">
                    <div class="gallery-overlay"><span>Latte Art</span></div>
                </div>
                <div class="gallery-item large" data-aos="fade-up" data-aos-delay="500">
                    <img src="assets/dessert-placeholder.jpg" alt="Desserts">
                    <div class="gallery-overlay"><span>Sweet Decadence</span></div>
                </div>
                <div class="gallery-item wide" data-aos="fade-up" data-aos-delay="600">
                    <img src="assets/turkish-coffee-quiet-cup-cafe.jpg" alt="Turkish Coffee">
                    <div class="gallery-overlay"><span>Signature Brews</span></div>
                </div>
                <div class="gallery-item" data-aos="fade-up" data-aos-delay="700">
                    <img src="assets/tea-placeholder.jpg" alt="Artisan Teas">
                    <div class="gallery-overlay"><span>Infusions</span></div>
                </div>
            </div>
        </section>
    </main>
'''

with open('gallery.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <main>...</main>
content = re.sub(r'<main>.*?</main>', gallery_main, content, flags=re.DOTALL)

# Set active link
content = content.replace('href="about.html" class="active"', 'href="about.html"')
content = content.replace('href="gallery.html"', 'href="gallery.html" class="active"')
content = content.replace('<title>The Quiet Cup Café | About Us</title>', '<title>The Quiet Cup Café | Gallery</title>')

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Gallery page built.")
