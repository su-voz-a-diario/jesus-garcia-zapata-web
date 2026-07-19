import os
import glob

html_files = glob.glob('/Volumes/Almacenamiento/jesus-garcia-zapata/*.html')

old_fb = '<a href="#" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>'
new_yt = '<a href="https://youtube.com/@jesusgarcia-x9h7f?si=NAqWkVvbL25dSlB5" aria-label="YouTube" target="_blank"><i class="fa-brands fa-youtube"></i></a>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_fb in content:
        content = content.replace(old_fb, new_yt)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(file)}")
