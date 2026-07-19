import re

with open('/Volumes/Almacenamiento/jesus-garcia-zapata/conferencias.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Hero background
old_bg = "background-image: url('https://images.unsplash.com/photo-1475721028314-390576a06141?q=80&w=1920&auto=format&fit=crop');"
new_bg = "background-image: url('assets/images/conferencias/conf-16.webp');"
content = content.replace(old_bg, new_bg)

# 2. Build the new gallery section
gallery_html = '''<section class="conference-gallery" style="margin-top: 5rem;">
            <h2 class="section-title">En Acción</h2>
            <p style="text-align: center; color: var(--gray-light); margin-bottom: 3rem;">Un vistazo a los proyectos, entrevistas y charlas compartidas.</p>
            <div class="gallery-grid" style="grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));">
'''

for i in range(1, 18):
    img_path = f'assets/images/conferencias/conf-{i:02d}.webp'
    gallery_html += f'''                <div class="gallery-item" style="border: none; background: transparent;">
                    <div class="gallery-img-container" style="border-radius: 8px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.5);">
                        <img src="{img_path}" loading="lazy" alt="Conferencia Jesús García Zapata {i}">
                    </div>
                </div>\n'''

gallery_html += '            </div>\n        </section>'

# Replace the conference-videos section with the new gallery_html
content = re.sub(r'<section class="conference-videos">.*?</section>', gallery_html, content, flags=re.DOTALL)

with open('/Volumes/Almacenamiento/jesus-garcia-zapata/conferencias.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("conferencias.html updated successfully with new photo gallery.")
