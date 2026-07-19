import os
import glob
from PIL import Image

input_dir = '/Volumes/Almacenamiento/jesus-garcia-zapata/Fotos de BADA'
output_dir = '/Volumes/Almacenamiento/jesus-garcia-zapata/assets/images/conferencias'
os.makedirs(output_dir, exist_ok=True)

images = glob.glob(os.path.join(input_dir, '*.jpg')) + glob.glob(os.path.join(input_dir, '*.jpeg')) + glob.glob(os.path.join(input_dir, '*.JPG'))

images.sort()

max_size = (1920, 1920)

for idx, img_path in enumerate(images, start=1):
    try:
        with Image.open(img_path) as img:
            # Correct orientation
            try:
                from PIL import ExifTags
                for orientation in ExifTags.TAGS.keys():
                    if ExifTags.TAGS[orientation] == 'Orientation':
                        break
                exif = img._getexif()
                if exif is not None:
                    exif_dict = dict(exif.items())
                    if orientation in exif_dict:
                        if exif_dict[orientation] == 3:
                            img = img.rotate(180, expand=True)
                        elif exif_dict[orientation] == 6:
                            img = img.rotate(270, expand=True)
                        elif exif_dict[orientation] == 8:
                            img = img.rotate(90, expand=True)
            except Exception as e:
                pass
            
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            output_path = os.path.join(output_dir, f'conf-{idx:02d}.webp')
            img.save(output_path, 'WEBP', quality=85)
            print(f"Optimized {os.path.basename(img_path)} -> conf-{idx:02d}.webp")
    except Exception as e:
        print(f"Error processing {img_path}: {e}")

print(f"Total processed: {len(images)}")
