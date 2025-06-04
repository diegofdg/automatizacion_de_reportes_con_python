import pandas as pd
import sys
import shutil
import os
from docxtpl import DocxTemplate

PATH_CARPETA = r'D:\mis_proyectos\ciencia_de_datos\automatizacion_de_reportes_con_python\project-excel'
PATH_OUTPUT = PATH_CARPETA + r'\outputs'

# Corresponde a nuestro Excel de cursos
NOTAS_ALUMNOS_PATH = PATH_CARPETA + r'\inputs\Notas_Alumnos.xlsx'

# Corresponde a nuestro Word de cursos
PLANTILLA_CURSOS_PATH = PATH_CARPETA + r'\inputs\Plantilla_Notas.docx'

CURSO = '2021/2022'

dict_asig = {
    'LENGUA CASTELLANA Y LITERATURA':   'Lengua Castellana y Literatura',
    'BIOLOGIA':                         'Biología',
    'GEOGRAFIA E HISTORIA':             'Geografía e Historia',
    'MATEMATICAS':                      'Matemáticas',
    'INGLES':                           'Inglés',
    'EDUCACION FISICA':                 'Educación Física',
    'ETICA':                            'Ética',
    'CULTURA CLASICA':                  'Cultura clásica',
    'MUSICA':                           'Música',
    'TECNOLOGIA':                       'Tecnología',
    'EDUCACION PLASTICA':               'Educación Plástica',
    'FRANCES':                          'Francés',
}

def deteccionErrores(df):
    err1, err2, err3 = False, False, False
    alumnos_list = sorted(list(df['NOMBRE'].drop_duplicates()))
    asignatura_list = sorted(list(df['ASIGNATURA'].drop_duplicates()))
    
    for al in alumnos_list:
        for asig in asignatura_list:
            filt_al_as_df = df[(df['NOMBRE'] == al) & (df['ASIGNATURA'] == asig)]
            
            if(len(filt_al_as_df) == 0):
                print(f'Error: El alumno {al} no tiene la asignatura {asig} asignada')
                err1 = True
            elif(len(filt_al_as_df) >1):
                print(f'Error: El alumno {al} tiene la asignatura {asig} repetida {len(filt_al_as_df)} veces')
                err2 = True
        
        for index, row in df.iterrows():
            trimestre_list = ['NOTA T1', 'NOTA T2', 'NOTA T3']
            for trim in trimestre_list:
                if not ((row[trim] >= 0.0) and (row[trim] <=10.0)):
                    print(f'Error: El alumno {al} tiene el campo {trim} de la asignatura {asig} fuera de rango {str(row[trim])}')
                    err3 = True
        
        if (err1 == True ) or (err2 == True) or (err3 == True):
            print('')
            print('Debes corregir los errores para continuar con la ejecucion del programa')
            sys.exit(1)
        else:
            print('Ningun error detectado ')


def eliminarTildes(texto):
    tildes_dict = {
        'Á': 'A',
        'É': 'E',
        'Í': 'I',
        'Ó': 'O',
        'Ú': 'U',
    }
    textoSinTildes = texto
    for key in tildes_dict:
        textoSinTildes = textoSinTildes.replace(key, tildes_dict[key])
    return textoSinTildes
    
def eliminarCrearCarpetas(path):
    if os.path.exists(path):
        shutil.rmtree(path)

    os.mkdir(path)

def crearWordAsignarTag(datos_alumnos, excel_df):
    asig_list = sorted(list(excel_df['ASIGNATURA'].drop_duplicates()))
        
    filter_td_asig = []
    for item in asig_list:
        valorTd = dict_asig[item]
        filter_td_asig.append(valorTd.upper())
    
    nombre_Alumno_list = sorted(list(datos_alumnos['NOMBRE']))
    
    for nombre_alumno in nombre_Alumno_list:
        # Cargar documento
        docs_tpl = DocxTemplate(PLANTILLA_CURSOS_PATH)
        
        filt_datos_alumnos_df = datos_alumnos[(datos_alumnos['NOMBRE'] == nombre_alumno)]
        clase = filt_datos_alumnos_df.iloc[0]['CLASE']
        
        # Crear tabla de notas
        asignatura_list = []
        
        # Iterar sobre los índices de asignaturas
        for asig_idx in range(len(asig_list)):
            asign = asig_list[asig_idx]
            filt_al_as_excel_df = excel_df[(excel_df['NOMBRE'] == nombre_alumno) & (excel_df['ASIGNATURA'] == asign)]
            print(filt_al_as_excel_df)
            
        # Context
        context = {
            'curso': CURSO,
            'nombre_alumno': nombre_alumno,
            'clase': clase
        }
        
        # Renderizamos el documento
        docs_tpl.render(context)
        titulo = 'NOTAS_' + nombre_alumno
        titulo = titulo.upper()
        titulo = eliminarTildes(titulo)
        titulo = titulo.replace(" ", "_")
        titulo += '.docx'
        
        # Guardamos el documento
        docs_tpl.save(PATH_OUTPUT + '\\' + titulo)

def main():    
    eliminarCrearCarpetas(PATH_OUTPUT)    
         
    # Leemos notas y datos alumnos 
    excel_df = pd.read_excel(NOTAS_ALUMNOS_PATH, sheet_name='Notas')
    datos_alumnos = pd.read_excel(NOTAS_ALUMNOS_PATH, sheet_name='Datos_Alumnos')
        
    # Detectamos errores
    deteccionErrores(excel_df)
    
    # Creamos y asignamos tags en el word
    crearWordAsignarTag(datos_alumnos, excel_df)
    
if __name__ == '__main__':
    main()