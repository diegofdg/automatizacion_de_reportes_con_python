from pathlib import Path

### Obtener un listado de archivos de un directorio por su extensión
carpeta = Path('project-path/nuevo_test')
paths = carpeta.glob('**/*.html')
for path in paths:
    print(path)

### Obtener un listado de archivos de un directorio
carpeta = Path('project-path/nuevo_test')
paths = carpeta.glob('**/*')
for path in paths:
    if path.is_file():
        print(f'El archivo encontrado es: {path}')
    else: 
        print('No hay archivos')