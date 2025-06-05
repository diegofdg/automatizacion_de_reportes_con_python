from pathlib import Path
import calendar

### Creamos una carpeta
Path('project-path/nueva_carpeta').mkdir(exist_ok=True)

### Creamos carpetas anidadas
Path('project-path/carpeta1/carpeta2/carpeta3').mkdir(parents=True, exist_ok=True)

### Creamos una carpeta por cada mes y por cada dia
meses_anio = list(calendar.month_name[1:])
dias_semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
for i, mes in enumerate(meses_anio):
    for dia in dias_semana:
        Path(f'project-path/2022/{i+1}.{mes}/{dia}').mkdir(parents=True, exist_ok=True)