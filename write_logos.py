import os

logos_dir = r"c:\Sample-Portfolio-Canva\assets\logos"
os.makedirs(logos_dir, exist_ok=True)

logos = {
    "realme.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 40" fill="#f2f4ed">
<rect x="6" y="8" width="24" height="24" rx="4" fill="none" stroke="#f2f4ed" stroke-width="3"/>
<path d="M14 26V14h5c2.5 0 4 1.5 4 3.5s-1.5 3-3 3.3l3.5 5.2h-3l-3-4.5h-1.5v4.5H14zm2-6.5h3c1.5 0 2.2-.6 2.2-1.7s-.7-1.8-2.2-1.8H16v3.5z"/>
<text x="38" y="27" font-family="'Space Grotesk', sans-serif" font-size="22" font-weight="700" letter-spacing="1">realme</text>
</svg>''',

    "hm.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 40" fill="#f2f4ed">
<path d="M10 8h5.5v10H27V8h5.5v24H27V22H15.5v10H10V8zm28 14c0-2 1.5-3.5 3.5-3.5 1.5 0 2.5.8 3 2l2.5-1.5c-1-2-3-3-5.5-3-3.5 0-6.5 2.5-6.5 6s3 6 6.5 6c2.5 0 4.5-1 5.5-3L44.5 23.5c-.5 1.2-1.5 2-3 2-2 0-3.5-1.5-3.5-3.5zm19-14H61l4.5 14L70 8h4.5l4.5 14L83.5 8H88l-6 24h-4.5L72 17l-5.5 15H62l-5-24z"/>
</svg>''',

    "snitch.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 40" fill="#f2f4ed">
<text x="50%" y="28" font-family="'Space Grotesk', sans-serif" font-size="28" font-weight="900" letter-spacing="4" text-anchor="middle">SNITCH</text>
</svg>''',

    "asianpaints.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 40" fill="#f2f4ed">
<path d="M8 28L16 8l8 20h-4.5l-3.5-9-3.5 9H8zm22-14h18v4H36v2.5h10v4H36v5.5h-6V14zm24 0h6v16h-6V14zm12 0h16v4h-5v12h-6V18h-5v-4zm22 16l-7-16h6.5l3.5 9 3.5-9H112l-7 16h-5z"/>
<text x="105" y="27" font-family="'Plus Jakarta Sans', sans-serif" font-size="20" font-weight="700" letter-spacing="0.5">asian paints</text>
</svg>''',

    "glenmark.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 40" fill="#f2f4ed">
<rect x="8" y="10" width="20" height="20" rx="3" fill="#c8ff48" fill-opacity="0.2" stroke="#c8ff48" stroke-width="2"/>
<path d="M18 14v12M12 20h12" stroke="#c8ff48" stroke-width="2" stroke-linecap="round"/>
<text x="36" y="27" font-family="'Plus Jakarta Sans', sans-serif" font-size="21" font-weight="700" letter-spacing="1">Glenmark</text>
</svg>''',

    "fabelle.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 40" fill="#f2f4ed">
<text x="50%" y="23" font-family="'Syne', sans-serif" font-size="21" font-weight="800" letter-spacing="4" text-anchor="middle">FABELLE</text>
<text x="50%" y="34" font-family="'Space Mono', monospace" font-size="8" font-weight="700" letter-spacing="3" text-anchor="middle" fill="#c8ff48">CHOCOLATES</text>
</svg>''',

    "lenskart.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 40" fill="#f2f4ed">
<circle cx="18" cy="20" r="10" stroke="#f2f4ed" stroke-width="2.5" fill="none"/>
<circle cx="44" cy="20" r="10" stroke="#f2f4ed" stroke-width="2.5" fill="none"/>
<path d="M28 20h6" stroke="#f2f4ed" stroke-width="2.5"/>
<text x="62" y="27" font-family="'Space Grotesk', sans-serif" font-size="22" font-weight="800" letter-spacing="1">lenskart</text>
</svg>''',

    "bonkers.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 40" fill="#f2f4ed">
<text x="50%" y="28" font-family="'Space Grotesk', sans-serif" font-size="26" font-weight="900" letter-spacing="3" text-anchor="middle">BONKERS</text>
</svg>''',

    "samsung.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 40" fill="#f2f4ed">
<ellipse cx="80" cy="20" rx="72" ry="16" fill="none" stroke="#f2f4ed" stroke-width="1.5" stroke-opacity="0.3"/>
<text x="50%" y="26" font-family="'Space Grotesk', sans-serif" font-size="20" font-weight="900" letter-spacing="4" text-anchor="middle">SAMSUNG</text>
</svg>''',

    "levis.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 40" fill="#f2f4ed">
<path d="M15 10c25 0 35-4 55-4s30 4 55 4v20c-25 0-35-4-55-4s-30 4-55 4V10z" fill="#ff3344" fill-opacity="0.85"/>
<text x="70" y="24" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="900" letter-spacing="2" text-anchor="middle" fill="#ffffff">LEVI'S</text>
</svg>''',

    "gshock.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 40" fill="#f2f4ed">
<path d="M10 8h24l6 6v12l-6 6H10l-6-6V14l6-6z" fill="none" stroke="#f2f4ed" stroke-width="2"/>
<text x="22" y="25" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="900">G</text>
<text x="50" y="26" font-family="'Space Grotesk', sans-serif" font-size="20" font-weight="900" letter-spacing="2">SHOCK</text>
</svg>'''
}

for name, svg_data in logos.items():
    file_path = os.path.join(logos_dir, name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(svg_data)
    print(f"Created {name}")

print("All logos successfully generated.")
