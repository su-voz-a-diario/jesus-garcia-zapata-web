import glob

css_addition = """
/* ==========================================================================
   MENÚ MÓVIL Y AJUSTES RESPONSIVOS GLOBALES
   ========================================================================== */
html, body {
    overflow-x: hidden;
    width: 100%;
}

@media (max-width: 768px) {
    .main-nav {
        display: none;
        position: absolute;
        top: 100%;
        left: 0;
        width: 100%;
        background-color: rgba(13, 13, 13, 0.98);
        padding: 2rem 0;
        border-bottom: 1px solid rgba(201, 169, 110, 0.3);
    }
    
    .main-nav.active {
        display: block;
    }
    
    .main-nav ul {
        flex-direction: column;
        align-items: center;
        gap: 1.5rem;
    }
    
    .gallery-grid {
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 1rem;
    }
    
    .topics-grid {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 480px) {
    .gallery-grid {
        grid-template-columns: 1fr;
    }
    
    .page-title {
        font-size: 2rem;
    }
}
"""

with open('/Volumes/Almacenamiento/jesus-garcia-zapata/styles.css', 'a', encoding='utf-8') as f:
    f.write(css_addition)

js_content = """
document.addEventListener('DOMContentLoaded', () => {
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mainNav = document.querySelector('.main-nav');
    
    if (mobileMenuBtn && mainNav) {
        mobileMenuBtn.addEventListener('click', () => {
            mainNav.classList.toggle('active');
            const icon = mobileMenuBtn.querySelector('i');
            if (mainNav.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-xmark');
            } else {
                icon.classList.remove('fa-xmark');
                icon.classList.add('fa-bars');
            }
        });
    }
});
"""

with open('/Volumes/Almacenamiento/jesus-garcia-zapata/mobile-menu.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

html_files = glob.glob('/Volumes/Almacenamiento/jesus-garcia-zapata/*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<script src="mobile-menu.js"></script>' not in content:
        content = content.replace('</body>', '    <script src="mobile-menu.js"></script>\n</body>')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Mobile menu JS and responsive CSS injected successfully.")
