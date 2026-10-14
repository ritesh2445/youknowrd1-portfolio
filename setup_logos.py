import os
import urllib.request

logos_dir = r"c:\Sample-Portfolio-Canva\assets\logos"
os.makedirs(logos_dir, exist_ok=True)

urls = {
    "adidas.svg": "https://cdn.jsdelivr.net/npm/simple-icons@v15/icons/adidas.svg",
    "realme.svg": "https://cdn.jsdelivr.net/npm/simple-icons@v15/icons/realme.svg",
    "hm.svg": "https://cdn.jsdelivr.net/npm/simple-icons@v15/icons/hm.svg",
    "samsung.svg": "https://cdn.jsdelivr.net/npm/simple-icons@v15/icons/samsung.svg",
    "levis.svg": "https://cdn.jsdelivr.net/npm/simple-icons@v15/icons/levis.svg",
    "budweiser.svg": "https://cdn.jsdelivr.net/npm/simple-icons@v15/icons/budweiser.svg",
    "gshock.svg": "https://cdn.jsdelivr.net/npm/simple-icons@v15/icons/casio.svg",
}

headers = {'User-Agent': 'Mozilla/5.0'}

for filename, url in urls.items():
    dest = os.path.join(logos_dir, filename)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response, open(dest, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

# Also create dedicated crisp vector SVGs for Indian & fashion brands
custom_logos = {
    "snitch.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 38" fill="#f2f4ed">
<text x="50%" y="28" font-family="'Space Grotesk', sans-serif" font-size="28" font-weight="900" letter-spacing="4" text-anchor="middle">SNITCH</text>
</svg>''',
    "asianpaints.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 38" fill="#f2f4ed">
<path d="M12 28L20 8l8 20h-4l-4-10-4 10h-4zm24-14h18v4H44v3h10v4H44v5h-8V14zm26 0h8v16h-8V14zm14 0h16v4h-8v12h-8V14zm24 16l-8-16h8l4 9 4-9h8l-8 16h-8z"/>
<text x="110" y="27" font-family="'Plus Jakarta Sans', sans-serif" font-size="20" font-weight="700" letter-spacing="1">asian paints</text>
</svg>''',
    "glenmark.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 38" fill="#f2f4ed">
<text x="50%" y="27" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="700" letter-spacing="1.5" text-anchor="middle">Glenmark</text>
</svg>''',
    "fabelle.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 38" fill="#f2f4ed">
<text x="50%" y="26" font-family="'Syne', sans-serif" font-size="22" font-weight="800" letter-spacing="4" text-anchor="middle">FABELLE</text>
<text x="50%" y="36" font-family="'Space Mono', monospace" font-size="8" letter-spacing="2" text-anchor="middle" fill="#c8ff48">CHOCOLATES</text>
</svg>''',
    "lenskart.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 38" fill="#f2f4ed">
<circle cx="22" cy="19" r="10" stroke="#f2f4ed" stroke-width="2.5" fill="none"/>
<circle cx="46" cy="19" r="10" stroke="#f2f4ed" stroke-width="2.5" fill="none"/>
<line x1="32" y1="19" x2="36" y2="19" stroke="#f2f4ed" stroke-width="2.5"/>
<text x="64" y="26" font-family="'Space Grotesk', sans-serif" font-size="22" font-weight="800" letter-spacing="1">lenskart</text>
</svg>''',
    "bonkers.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 38" fill="#f2f4ed">
<text x="50%" y="27" font-family="'Space Grotesk', sans-serif" font-size="24" font-weight="900" letter-spacing="3" text-anchor="middle">BONKERS</text>
</svg>'''
}

for filename, content in custom_logos.items():
    dest = os.path.join(logos_dir, filename)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created custom vector logo {filename}")
