from pathlib import Path

### Renombrando una carpeta
path = Path('project-path/test')
path.rename('project-path/nuevo_test')

### Renombrar archivo dentro de una carpeta
path = Path('project-path/nuevo_test/gastos.txt')
nuevoNombreCarpeta = path.with_name('gastos_diciembre.txt')
path.rename(nuevoNombreCarpeta)

### Obtener path de los subdirectorios inmediatos
carpeta = Path('project-path/2022')
for path in list(carpeta.iterdir()):
    print(path)

### Obtener path de todos los subdirectorios
carpeta = Path('project-path/2022')
paths = carpeta.glob('**/*')
for path in paths:
    print(path)