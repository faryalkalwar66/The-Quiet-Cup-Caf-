import glob
import re

preloader_html = '''
    <!-- Preloader & Magic Cursor -->
    <div id="preloader" class="preloader"><div class="loader"></div></div>
    <div id="custom-cursor" class="cursor"></div>
    <div id="cursor-follower" class="cursor-follower"></div>
'''

club_html = '''
        <div class="footer-club" data-aos="fade-up">
            <h3>The Quiet Club</h3>
            <p>Join our exclusive newsletter for hidden menus, early access, and free coffee perks.</p>
            <form class="club-form" onsubmit="event.preventDefault(); alert('Welcome to The Quiet Club!');">
                <input type="email" placeholder="Enter your email..." required>
                <button type="submit">Join</button>
            </form>
        </div>
'''

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    # 1. Add AOS CSS
    if 'aos.css' not in content:
        content = content.replace('</head>', '    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">\\n</head>')
    
    # 2. Add AOS JS
    if 'aos.js' not in content:
        content = content.replace('</body>', '    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>\\n</body>')
        
    # 3. Add Preloader and Cursor
    if 'id="preloader"' not in content:
        content = content.replace('<body>', f'<body>\\n{preloader_html}')
        
    # 4. Add The Quiet Club to Footer
    if 'footer-club' not in content:
        content = content.replace('<div class="footer-about">', f'{club_html}\\n        <div class="footer-about">')
        
    # 5. Add Gallery Link
    if 'gallery.html' not in content:
        content = content.replace('<li><a href="reviews.html">Reviews</a></li>', '<li><a href="reviews.html">Reviews</a></li>\\n                <li><a href="gallery.html">Gallery</a></li>')
        
    # 6. Replace animate-in with AOS
    content = content.replace(' animate-in', '" data-aos="fade-up')
    content = content.replace('class="animate-in"', 'data-aos="fade-up"')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("HTML injection complete.")
