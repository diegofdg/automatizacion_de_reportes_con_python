from pathlib import Path
import zipfile

### Extraer zip
directorio_actual = Path('project-path/')
directorio_objetivo = Path('project-path/temp')

for path in directorio_actual.glob('*.zip'):
    with zipfile.ZipFile(path, 'r') as zipObj:
        zipObj.extractall(path = directorio_objetivo)