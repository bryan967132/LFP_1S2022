from tkinter.filedialog import askopenfilename as openfile
from analisis import graph
from pData import parseData
from pLFP import parseLFP
class menu:
    def menuP(self):
        data = parseData()
        lfp = parseLFP()
        opcion = 0
        info = ""
        inst = ""
        while opcion != 5:
            try:
                self.opciones()
                opcion = int(input('Opcion: '))
                if opcion == 1:
                    arch = openfile()
                    info = data.datadec(arch).upper()
                    print('\nData Guardada\n')
                elif opcion == 2:
                    arch = openfile()
                    inst = lfp.datadec(arch).upper()
                    print('\nInstrucciones Guardadas\n')
                elif opcion == 3:
                    gr = graph()
                    gr.graphs(info,inst)
                    print('\nGráfica Generada\n')
                elif opcion == 4:
                    print('\nReporte Generado\n')
                elif opcion == 5:
                    print('\n¡Finalizado!\n')
                else:
                    print('\nSolo números entre 1 y 5\n')
            except:
                print('\nOpcion inválida\n')
    
    def opciones(self):
        print('Menú Principal')
        print('1. Cargar Data')
        print('2. Cargar Instrucciones')
        print('3. Analizar')
        print('4. Reportes')
        print('5. Salir')