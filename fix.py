import glob

replacements = {
    'CafAcAc': 'Café',
    'CafAc': 'Café',
    'Caf': 'Café',
    'dYOT': '🌙',
    'dY>''': '🛒',
    'Menu -_': 'Menu ▾',
    'dY" Download Menu': '📥 Download Menu',
    'Menu ?': 'Menu ▾',
    '?? Download Menu': '📥 Download Menu'
}

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
