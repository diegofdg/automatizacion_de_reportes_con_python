from pathlib import Path
import calendar

### Creamos una carpeta
# Path('project-path/nueva_carpeta').mkdir(exist_ok=True)

### Creamos carpetas anidadas
# Path('project-path/carpeta1/carpeta2/carpeta3').mkdir(parents=True, exist_ok=True)

### Creamos una carpeta por cada mes y por cada dia
# meses_anio = list(calendar.month_name[1:])
# dias_semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
# for i, mes in enumerate(meses_anio):
    # for dia in dias_semana:
        # Path(f'project-path/2022/{i+1}.{mes}/{dia}').mkdir(parents=True, exist_ok=True)

### Renombrando una carpeta
# path = Path('project-path/test')
# path.rename('project-path/nuevo_test')

### Renombrar archivo dentro de una carpeta
# path = Path('project-path/nuevo_test/gastos.txt')
# nuevoNombreCarpeta = path.with_name('gastos_diciembre.txt')
# path.rename(nuevoNombreCarpeta)

### Obtener path de los subdirectorios inmediatos
# carpeta = Path('project-path/2022')
# for path in list(carpeta.iterdir()):
    # print(path)

### Obtener path de todos los subdirectorios
# carpeta = Path('project-path/2022')
# paths = carpeta.glob('**/*')
# for path in paths:
    # print(path)

### Obtener un listado de archivos de un directorio por su extensión
# carpeta = Path('project-path/nuevo_test')
# paths = carpeta.glob('**/*.html')
# for path in paths:
    # print(path)

### Obtener un listado de archivos de un directorio
carpeta = Path('project-path/nuevo_test')
paths = carpeta.glob('**/*')
for path in paths:
    if path.is_file():
        print(f'El archivo encontrado es: {path}')
    else: 
        print('No hay archivos')