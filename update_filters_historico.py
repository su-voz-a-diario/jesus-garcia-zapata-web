import re

with open('/Volumes/Almacenamiento/jesus-garcia-zapata/obras.html', 'r', encoding='utf-8') as f:
    content = f.read()

gallery_html = '<div class="gallery-grid" id="gallery-grid">\n'

# 1. Add available artworks (1 to 15)
for i in range(1, 16):
    img_name = f'obra-jesus-garcia-zapata-{i:02d}.webp'
    gallery_html += f'''                <div class="gallery-item" data-category="adquisicion">
                    <div class="gallery-img-container">
                        <img src="assets/images/obras/{img_name}" loading="lazy" alt="Obra Original {i}">
                        <div class="gallery-hover">
                            <i class="fa-solid fa-magnifying-glass-plus"></i>
                        </div>
                    </div>
                    <div class="gallery-info">
                        <h3 class="gallery-item-title">Obra Original #{i:02d}</h3>
                        <p class="gallery-item-meta">Técnica mixta</p>
                        <span class="status-badge status-available" style="margin-bottom: 0.5rem; display: inline-block;">Disponible</span>
                        <a href="tienda.html" class="btn btn-card" style="font-size: 0.8rem; padding: 0.4rem 0.8rem; margin-top: 0.5rem; display: block;">Adquirir Obra</a>
                    </div>
                </div>\n'''

# 2. Add historical artworks (1 to 23)
for i in range(1, 24):
    img_name = f'historico-{i:02d}.webp'
    gallery_html += f'''                <div class="gallery-item" data-category="historico">
                    <div class="gallery-img-container">
                        <img src="assets/images/obras/{img_name}" loading="lazy" alt="Archivo Histórico {i}">
                        <div class="gallery-hover">
                            <i class="fa-solid fa-magnifying-glass-plus"></i>
                        </div>
                    </div>
                    <div class="gallery-info">
                        <h3 class="gallery-item-title">Archivo Histórico #{i:02d}</h3>
                        <p class="gallery-item-meta">Técnica mixta</p>
                        <span class="status-badge" style="background-color: var(--gray-dark); color: var(--gray-light); margin-bottom: 0.5rem; display: inline-block; padding: 0.3rem 0.6rem; border-radius: 4px; font-size: 0.8rem; font-weight: 500;">Colección Privada</span>
                    </div>
                </div>\n'''

gallery_html += '\n            </div>'

# Replace old gallery-grid completely.
content = re.sub(r'<div class="gallery-grid" id="gallery-grid">.*?(?=<section class="commissions-section")', gallery_html + '\n            ', content, flags=re.DOTALL)
content = re.sub(r'<div class="gallery-grid">.*?(?=<section class="commissions-section")', gallery_html + '\n            ', content, flags=re.DOTALL)

with open('/Volumes/Almacenamiento/jesus-garcia-zapata/obras.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated obras.html with historical items and no empty state.")
