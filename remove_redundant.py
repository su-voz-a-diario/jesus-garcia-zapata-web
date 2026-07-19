import os
import glob

html_files = glob.glob('/Volumes/Almacenamiento/jesus-garcia-zapata/*.html')

redundant_link = '                        <a href="#" aria-label="YouTube"><i class="fa-brands fa-youtube"></i></a>\n'
redundant_link2 = '                <a href="#" aria-label="YouTube"><i class="fa-brands fa-youtube"></i></a>\n'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if redundant_link in content or redundant_link2 in content:
        content = content.replace(redundant_link, '')
        content = content.replace(redundant_link2, '')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Removed redundant link from {os.path.basename(file)}")
