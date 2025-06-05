from pathlib import Path

### Cambiar extensión de un archivo
folder = Path('project-path/extensiones')

# Pasar de txt a csv
for path in list(folder.iterdir()):
    if path.suffix == '.txt':
        nuevoNombreExtension = path.with_suffix('.csv')
        path.rename(nuevoNombreExtension)

# Pasar de csv a txt
for path in folder.glob('**/*.csv'):    
    nuevoNombreExtension = path.with_suffix('.txt')
    path.rename(nuevoNombreExtension)