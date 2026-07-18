import re

with open('/Volumes/Almacenamiento/jesus-garcia-zapata/obras.html', 'r') as f:
    content = f.read()

new_filters = '''<div class="gallery-filters">
                <button class="filter-btn active" data-filter="all">Catálogo Completo</button>
                <button class="filter-btn" data-filter="adquisicion">En Adquisición</button>
                <button class="filter-btn" data-filter="historico">Archivo Histórico</button>
            </div>'''
content = re.sub(r'<div class="gallery-filters">.*?</div>', new_filters, content, flags=re.DOTALL)

items = re.split(r'(<div class="gallery-item">)', content)
for i in range(1, len(items), 2):
    cat = "adquisicion" if (i//2) % 2 == 0 else "historico"
    items[i] = f'<div class="gallery-item" data-category="{cat}">'
    if cat == "historico":
        items[i+1] = items[i+1].replace('Disponible', 'Colección Privada').replace('status-available', 'status-sold')

content = "".join(items)

custom_block = '''</div>
            
            <section class="commissions-section" style="margin-top: 5rem; padding: 4rem 2rem; background: var(--bg-dark); border-radius: 8px; text-align: center; border: 1px solid var(--gray-medium);">
                <h2 class="section-title">Comisiones Especiales</h2>
                <p style="color: var(--gray-light); margin-bottom: 2rem; max-width: 600px; margin-left: auto; margin-right: auto; line-height: 1.6;">¿Tienes una idea en mente? Convierte tu visión, un recuerdo o un retrato en una obra de arte original pintada a tu medida por Jesús García Zapata.</p>
                <a href="contacto.html" class="btn btn-primary">Contáctame para tu obra</a>
            </section>
        </div>'''
content = content.replace('</div>\n        </div>\n    </main>', f'{custom_block}\n    </main>')

filter_js = '''
            // Filter logic
            const filterBtns = document.querySelectorAll('.filter-btn');
            const galleryItems = document.querySelectorAll('.gallery-item');

            filterBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    filterBtns.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');

                    const filterValue = btn.getAttribute('data-filter');

                    galleryItems.forEach(item => {
                        if (filterValue === 'all' || item.getAttribute('data-category') === filterValue) {
                            item.style.display = 'block';
                        } else {
                            item.style.display = 'none';
                        }
                    });
                });
            });
'''
content = content.replace("const galleryContainers = document.querySelectorAll('.gallery-img-container');", filter_js + "\n            const galleryContainers = document.querySelectorAll('.gallery-img-container');")

with open('/Volumes/Almacenamiento/jesus-garcia-zapata/obras.html', 'w') as f:
    f.write(content)
print("Updated obras.html")
