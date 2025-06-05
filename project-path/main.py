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
# carpeta = Path('project-path/nuevo_test')
# paths = carpeta.glob('**/*')
# for path in paths:
    # if path.is_file():
        # print(f'El archivo encontrado es: {path}')
    # else: 
        # print('No hay archivos')
        
### Cambiar extensión de un archivo
# folder = Path('project-path/extensiones')

# Pasar de txt a csv
# for path in list(folder.iterdir()):
    # if path.suffix == '.txt':
        # nuevoNombreExtension = path.with_suffix('.csv')
        # path.rename(nuevoNombreExtension)

# Pasar de csv a txt
# for path in folder.glob('**/*.csv'):    
    # nuevoNombreExtension = path.with_suffix('.txt')
    # path.rename(nuevoNombreExtension)

### Crear ficheros
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in numeros:
    # with open ('project-path/test/' + f'test{i}.txt', 'w') as file:
        # file.write('Hola Mundo')

### Eliminar todos los archivos .txt
# for path in Path('project-path/test/').glob('*.txt'):
    # path.unlink()

### Eliminar todos los archivos .txt menos el test9
for path in Path('project-path/test/').glob('test[1-8].txt'):
    path.unlink()
 