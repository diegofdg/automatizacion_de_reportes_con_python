import pandas as pd
PATH_CARPETA = r'D:\mis_proyectos\ciencia_de_datos\automatizacion_de_reportes_con_python\project-excel\inputs'

NOTAS_ALUMNOS_PATH = PATH_CARPETA + r'\Notas_Alumnos.xlsx'

def main():
    excel_df = pd.read_excel(NOTAS_ALUMNOS_PATH, sheet_name='Notas')
    for index, row in excel_df.iterrows():
        print(index, row['NOMBRE'])
        
    asig_list = sorted(list(excel_df['ASIGNATURA'].drop_duplicates()))
    print(asig_list)
    
if __name__ == '__main__':
    main()