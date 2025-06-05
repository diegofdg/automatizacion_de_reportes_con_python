from pathlib import Path

### Crear ficheros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in numeros:
    with open ('project-path/test/' + f'test{i}.txt', 'w') as file:
        file.write('Hola Mundo')

### Eliminar todos los archivos .txt
for path in Path('project-path/test/').glob('*.txt'):
    path.unlink()

### Eliminar todos los archivos .txt menos el test9
for path in Path('project-path/test/').glob('test[1-8].txt'):
    path.unlink()