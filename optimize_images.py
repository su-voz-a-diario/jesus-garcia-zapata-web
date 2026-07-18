import os
import glob
from PIL import Image

def process_images():
    source_dir = '/Volumes/Almacenamiento/jesus-garcia-zapata/pinturas'
    dest_dir = '/Volumes/Almacenamiento/jesus-garcia-zapata/assets/images/obras'
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        
    images = glob.glob(os.path.join(source_dir, '*.jpeg')) + glob.glob(os.path.join(source_dir, '*.jpg'))
    
    for i, img_path in enumerate(sorted(images)):
        try:
            with Image.open(img_path) as img:
                # Convert to RGB in case it's RGBA
                rgb_im = img.convert('RGB')
                
                # Resize if too large (max 2000px as per requirements)
                max_size = 2000
                if max(rgb_im.size) > max_size:
                    rgb_im.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
                
                # Generate new SEO friendly name
                new_filename = f'obra-jesus-garcia-zapata-{i+1:02d}.webp'
                dest_path = os.path.join(dest_dir, new_filename)
                
                # Save as WebP
                rgb_im.save(dest_path, 'WEBP', quality=85)
                print(f"✅ Procesada y convertida: {new_filename}")
                
        except Exception as e:
            print(f"❌ Error al procesar {img_path}: {e}")

if __name__ == "__main__":
    process_images()
