import re

with open('/Volumes/Almacenamiento/jesus-garcia-zapata/obras.html', 'r') as f:
    content = f.read()

# Make sure we don't duplicate filters if already there
# We'll regenerate the whole gallery-grid based on images 1 to 15
gallery_html = '<div class="gallery-grid" id="gallery-grid">\n'

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
                        <a href="tienda.html" class="btn btn-card" style="font-size: 0.8rem; padding: 0.4rem 0.8rem; margin-top: 0.5rem; display: block;">Adquirir en Tienda</a>
                    </div>
                </div>\n'''

# Add an empty state message
gallery_html += '''                <div id="empty-state" style="display: none; grid-column: 1 / -1; text-align: center; padding: 4rem 1rem;">
                    <i class="fa-solid fa-image" style="font-size: 3rem; color: var(--gray-medium); margin-bottom: 1rem;"></i>
                    <h3 style="color: var(--white); margin-bottom: 0.5rem;">Galería en construcción</h3>
                    <p style="color: var(--gray-light);">Próximamente el artista compartirá más fotografías de su archivo histórico.</p>
                </div>'''
gallery_html += '\n            </div>'

# Replace old gallery-grid completely. Note: It's important to not delete the comissions section we just added.
# The comissions section starts with <section class="commissions-section".
# So we replace from <div class="gallery-grid" to <section class="commissions-section"
content = re.sub(r'<div class="gallery-grid">.*?(?=<section class="commissions-section")', gallery_html + '\n            ', content, flags=re.DOTALL)
# Also fix if it was already updated with id="gallery-grid"
content = re.sub(r'<div class="gallery-grid" id="gallery-grid">.*?(?=<section class="commissions-section")', gallery_html + '\n            ', content, flags=re.DOTALL)


# Update JS logic to handle empty state
filter_js = '''
            // Filter logic
            const filterBtns = document.querySelectorAll('.filter-btn');
            const galleryItems = document.querySelectorAll('.gallery-item');
            const emptyState = document.getElementById('empty-state');

            filterBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    filterBtns.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');

                    const filterValue = btn.getAttribute('data-filter');
                    let count = 0;

                    galleryItems.forEach(item => {
                        if (filterValue === 'all' || item.getAttribute('data-category') === filterValue) {
                            item.style.display = 'block';
                            count++;
                        } else {
                            item.style.display = 'none';
                        }
                    });
                    
                    if(emptyState) {
                        emptyState.style.display = count === 0 ? 'block' : 'none';
                    }
                });
            });
'''
# Replace old script logic
content = re.sub(r'// Filter logic.*?}\);', filter_js, content, flags=re.DOTALL)

with open('/Volumes/Almacenamiento/jesus-garcia-zapata/obras.html', 'w') as f:
    f.write(content)
print("Updated obras.html with new filters and empty state")
