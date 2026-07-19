import glob

# 1. Update tienda.html
with open('/Volumes/Almacenamiento/jesus-garcia-zapata/tienda.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('Añadir al Carrito', 'Adquirir Obra')
with open('/Volumes/Almacenamiento/jesus-garcia-zapata/tienda.html', 'w', encoding='utf-8') as f:
    f.write(content)


# 2. Update obras.html
with open('/Volumes/Almacenamiento/jesus-garcia-zapata/obras.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('Adquirir en Tienda', 'Adquirir Obra')
with open('/Volumes/Almacenamiento/jesus-garcia-zapata/obras.html', 'w', encoding='utf-8') as f:
    f.write(content)


# 3. Update update_filters.py so future updates keep the text
with open('/Volumes/Almacenamiento/jesus-garcia-zapata/update_filters.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('Adquirir en Tienda', 'Adquirir Obra')
with open('/Volumes/Almacenamiento/jesus-garcia-zapata/update_filters.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Text replaced.")
