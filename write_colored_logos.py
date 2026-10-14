import os

logos_dir = r"c:\Sample-Portfolio-Canva\assets\logos"
os.makedirs(logos_dir, exist_ok=True)

# Official full-color brand logos
colored_logos = {
    # 1. Adidas (Iconic 3-Stripes in crisp White with subtle Lime accent)
    "adidas.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 50">
  <g fill="#ffffff">
    <path d="M42 34l8-14c1-1.8 3.3-2.4 5.1-1.4l.4.3c1.8 1 2.4 3.3 1.4 5.1l-8 14c-1 1.8-3.3 2.4-5.1 1.4l-.4-.3c-1.8-1-2.4-3.3-1.4-5.1z"/>
    <path d="M26 34l12-21c1-1.8 3.3-2.4 5.1-1.4l.4.3c1.8 1 2.4 3.3 1.4 5.1l-12 21c-1 1.8-3.3 2.4-5.1 1.4l-.4-.3c-1.8-1-2.4-3.3-1.4-5.1z"/>
    <path d="M10 34l16-28c1-1.8 3.3-2.4 5.1-1.4l.4.3c1.8 1 2.4 3.3 1.4 5.1L17 38c-1 1.8-3.3 2.4-5.1 1.4l-.4-.3c-1.8-1-2.4-3.3-1.4-5.1z"/>
  </g>
  <text x="66" y="34" font-family="'Space Grotesk', sans-serif" font-size="22" font-weight="900" fill="#ffffff" letter-spacing="2">adidas</text>
</svg>''',

    # 2. Realme (Official Realme Yellow #FFC915)
    "realme.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 50">
  <rect x="6" y="10" width="30" height="30" rx="6" fill="#FFC915"/>
  <path d="M16 32V18h6c3.2 0 5 1.8 5 4.3 0 1.9-1.2 3.4-3 3.9l3.5 5.8h-3.4l-3.1-5.1h-1.8V32H16zm3.2-7.5h2.5c1.4 0 2.2-.7 2.2-2s-.8-2-2.2-2h-2.5v4z" fill="#000000"/>
  <text x="44" y="33" font-family="'Space Grotesk', sans-serif" font-size="24" font-weight="800" fill="#FFC915" letter-spacing="1">realme</text>
</svg>''',

    # 3. H&M (Official H&M Red #E50010)
    "hm.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 130 50">
  <g fill="#E50010">
    <path d="M10 10h6.5v12h14V10H37v28h-6.5V26h-14v12H10V10zm33 16c0-2.5 1.8-4.2 4.2-4.2 2 0 3.2 1 3.8 2.5l3-1.8c-1.2-2.5-3.8-3.8-6.8-3.8-4.5 0-8 3.2-8 7.5s3.5 7.5 8 7.5c3 0 5.6-1.3 6.8-3.8l-3-1.8c-.6 1.5-1.8 2.5-3.8 2.5-2.4 0-4.2-1.7-4.2-4.6zm23-16h4.5l5.5 16.5L81.5 10H86l5.5 16.5L97 10h5.5l-7.5 28H90l-5.8-17.5L78.5 38H73.5L66 10z"/>
  </g>
</svg>''',

    # 4. SNITCH (Official Bold Black & Red Streetwear badge)
    "snitch.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 50">
  <rect x="4" y="10" width="152" height="30" rx="6" fill="#18181c" stroke="#ff3344" stroke-width="1.5"/>
  <text x="50%" y="32" font-family="'Space Grotesk', sans-serif" font-size="22" font-weight="900" fill="#ffffff" letter-spacing="5" text-anchor="middle">SNITCH</text>
  <circle cx="140" cy="25" r="3" fill="#ff3344"/>
</svg>''',

    # 5. Asian Paints (Official Crimson & Yellow Ribbon)
    "asianpaints.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 190 50">
  <path d="M8 35L17 11l9 24h-5.5l-3.5-9.5-3.5 9.5H8z" fill="#E31E24"/>
  <path d="M26 11l6 16 6-16h5.5l-9 24h-5.5l-8.5-24H26z" fill="#FFC915"/>
  <text x="56" y="33" font-family="'Plus Jakarta Sans', sans-serif" font-size="20" font-weight="800" fill="#ffffff">asian</text>
  <text x="110" y="33" font-family="'Plus Jakarta Sans', sans-serif" font-size="20" font-weight="800" fill="#E31E24">paints</text>
</svg>''',

    # 6. Glenmark (Official Cyan & Royal Blue Pharma cross)
    "glenmark.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 50">
  <rect x="6" y="12" width="26" height="26" rx="6" fill="#0072CE"/>
  <path d="M19 17v16M11 25h16" stroke="#ffffff" stroke-width="3.5" stroke-linecap="round"/>
  <text x="40" y="32" font-family="'Plus Jakarta Sans', sans-serif" font-size="22" font-weight="800" fill="#ffffff" letter-spacing="1">Glenmark</text>
</svg>''',

    # 7. Fabelle (Official Luxury Gold #D4AF37)
    "fabelle.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 50">
  <text x="50%" y="27" font-family="'Syne', sans-serif" font-size="22" font-weight="900" fill="#D4AF37" letter-spacing="4" text-anchor="middle">FABELLE</text>
  <text x="50%" y="40" font-family="'Space Mono', monospace" font-size="8" font-weight="700" letter-spacing="3" text-anchor="middle" fill="#c8ff48">FINE CHOCOLATES</text>
</svg>''',

    # 8. Lenskart (Official Electric Cyan #00BAC6 & Deep Navy)
    "lenskart.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 50">
  <circle cx="20" cy="25" r="11" stroke="#00BAC6" stroke-width="3" fill="none"/>
  <circle cx="48" cy="25" r="11" stroke="#00BAC6" stroke-width="3" fill="none"/>
  <path d="M31 25h6" stroke="#00BAC6" stroke-width="3"/>
  <text x="68" y="33" font-family="'Space Grotesk', sans-serif" font-size="24" font-weight="800" fill="#ffffff" letter-spacing="1">lenskart</text>
</svg>''',

    # 9. Bonkers (Official Streetwear Neon Lime & White)
    "bonkers.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 50">
  <text x="50%" y="33" font-family="'Space Grotesk', sans-serif" font-size="25" font-weight="900" fill="#c8ff48" letter-spacing="3" text-anchor="middle">BONKERS</text>
  <rect x="25" y="40" width="120" height="2" fill="#c8ff48"/>
</svg>''',

    # 10. Samsung (Official Samsung Blue #1428A0)
    "samsung.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 170 50">
  <ellipse cx="85" cy="25" rx="76" ry="18" fill="#1428A0"/>
  <text x="50%" y="32" font-family="'Space Grotesk', sans-serif" font-size="20" font-weight="900" fill="#ffffff" letter-spacing="3" text-anchor="middle">SAMSUNG</text>
</svg>''',

    # 11. Levi's (Official Red Batwing #C41230)
    "levis.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 150 50">
  <path d="M15 12c28 0 40-5 60-5s32 5 60 5v26c-28 0-40-5-60-5s-32 5-60 5V12z" fill="#C41230"/>
  <text x="75" y="29" font-family="'Space Grotesk', sans-serif" font-size="18" font-weight="900" fill="#ffffff" letter-spacing="2" text-anchor="middle">LEVI'S</text>
</svg>''',

    # 12. G-Shock (Official G-Shock Red #D90000 & White)
    "gshock.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 50">
  <path d="M12 10h24l7 7v16l-7 7H12l-7-7V17l7-7z" fill="#D90000"/>
  <text x="24" y="32" font-family="'Space Grotesk', sans-serif" font-size="17" font-weight="900" fill="#ffffff">G</text>
  <text x="54" y="33" font-family="'Space Grotesk', sans-serif" font-size="22" font-weight="900" fill="#ffffff" letter-spacing="2">SHOCK</text>
</svg>'''
}

for name, svg in colored_logos.items():
    with open(os.path.join(logos_dir, name), "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated colored logo {name}")

print("All colored logos generated.")
