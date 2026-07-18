import glob

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    # Fix literal \n
    content = content.replace('\\n</head>', '\n</head>')
    content = content.replace('\\n</body>', '\n</body>')
    content = content.replace('<body>\\n', '<body>\n')
    content = content.replace('\\n        <div class="footer-about">', '\n        <div class="footer-about">')
    content = content.replace('Reviews</a></li>\\n                <li><a href="gallery.html">', 'Reviews</a></li>\n                <li><a href="gallery.html">')
    
    # Fix Script order
    content = content.replace(
        '<script src="script.js"></script>\n    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>',
        '<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>\n    <script src="script.js"></script>'
    )
    
    # If it was still literal \n
    content = content.replace(
        '<script src="script.js"></script>\n    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>\n</body>',
        '<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>\n    <script src="script.js"></script>\n</body>'
    )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("HTML script order and newlines fixed.")
