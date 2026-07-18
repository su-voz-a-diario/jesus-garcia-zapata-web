import re

obras_file = '/Volumes/Almacenamiento/jesus-garcia-zapata/obras.html'
tienda_file = '/Volumes/Almacenamiento/jesus-garcia-zapata/tienda.html'

with open(obras_file, 'r') as f:
    obras_content = f.read()

with open(tienda_file, 'r') as f:
    tienda_content = f.read()

gallery_html = '<div class="gallery-grid">\n'
shop_html = '<div class="shop-grid">\n'

for i in range(1, 16):
    img_name = f'obra-jesus-garcia-zapata-{i:02d}.webp'
    gallery_html += f'''                <div class="gallery-item">
                    <div class="gallery-img-container">
                        <img src="assets/images/obras/{img_name}" loading="lazy" alt="Obra Original {i}">
                        <div class="gallery-hover">
                            <i class="fa-solid fa-magnifying-glass-plus"></i>
                        </div>
                    </div>
                    <div class="gallery-info">
                        <h3 class="gallery-item-title">Obra Original #{i:02d}</h3>
                        <p class="gallery-item-meta">Técnica mixta</p>
                        <span class="status-badge status-available">Disponible</span>
                    </div>
                </div>\n'''

    shop_html += f'''            <div class="shop-item">
                <div class="shop-img-container">
                    <span class="unique-badge">Pieza Única</span>
                    <img src="assets/images/obras/{img_name}" loading="lazy" alt="Obra Original {i}">
                    <div class="shop-hover">
                        <button class="btn btn-primary" style="width: 100%;">Añadir al Carrito</button>
                    </div>
                </div>
                <div class="shop-info">
                    <h3 class="shop-item-title">Obra Original #{i:02d}</h3>
                    <p class="shop-item-desc">Pintura original con certificado de autenticidad.</p>
                    <p class="shop-item-price">$15,000 MXN</p>
                </div>
            </div>\n'''

gallery_html += '            </div>'
shop_html += '        </div>'

# Regex replacement
obras_new = re.sub(r'<div class="gallery-grid">.*?</div>\n        </div>\n    </main>', f'{gallery_html}\n        </div>\n    </main>', obras_content, flags=re.DOTALL)
tienda_new = re.sub(r'<div class="shop-grid">.*?</div>\n        </div>\n    </main>', f'{shop_html}\n        </div>\n    </main>', tienda_content, flags=re.DOTALL)

with open(obras_file, 'w') as f:
    f.write(obras_new)

with open(tienda_file, 'w') as f:
    f.write(tienda_new)

print("HTMLs updated successfully")
