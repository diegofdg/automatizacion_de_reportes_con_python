import pandas as pd
import sys
from docxtpl import DocxTemplate

PATH_CARPETA = r'D:\mis_proyectos\ciencia_de_datos\automatizacion_de_reportes_con_python\project-excel'

NOTAS_ALUMNOS_PATH = PATH_CARPETA + r'\inputs\Notas_Alumnos.xlsx'
PLANTILLA_CURSOS_PATH = PATH_CARPETA + r'\inputs\Plantilla_Notas.docx'
PATH_OUTPUT = PATH_CARPETA + r'\outputs'

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
            #print(filt_al_as_df)
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


def main():
    # Cargar documento
    docs_tpl = DocxTemplate(PLANTILLA_CURSOS_PATH)
    
    # Context
    context = {
        'curso': "2021 / 2022",
        'nombre_alumno': 'Enrique Rodriguez',
        'clase': '4-C'
    }
    
    # Renderizamos el documento
    docs_tpl.render(context)
    
    # Guardamos el documento
    docs_tpl.save(PATH_OUTPUT + r'\fichero_word.docx')
     
    excel_df = pd.read_excel(NOTAS_ALUMNOS_PATH, sheet_name='Notas')
    for index, row in excel_df.iterrows():
        #print(index, row['NOMBRE'])
        pass
        
    asig_list = sorted(list(excel_df['ASIGNATURA'].drop_duplicates()))
    #print(asig_list)
    
    filter_td_asig = []
    for item in asig_list:
        valorTd = dict_asig[item]
        filter_td_asig.append(valorTd)
    #print(filter_td_asig)
    
    deteccionErrores(excel_df)
    
if __name__ == '__main__':
    main()