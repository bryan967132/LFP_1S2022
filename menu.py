from analisis import graph
from reporte import reporte
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
                    info = data.datadec()
                    print('\nData Guardada\n')
                elif opcion == 2:
                    try:
                        inst = lfp.datadec()
                        lfp.getBody(inst)['NOMBRE']
                        lfp.getBody(inst)['GRAFICA']
                        print('\nInstrucciones Guardadas\n')
                    except:
                        print('\nFaltan Datos Obligatorios\n')
                elif opcion == 3:
                    if inst != "" and info != "":
                        gr = graph()
                        gr.graphs(info,inst)
                        print('\nGráfica Generada\n')
                    else:
                        print('\nNo Se Han Cargado Instrucciones o Data\n')
                elif opcion == 4:
                    try:
                        if info != "":
                            rpt = reporte()
                            rpt.reportar(data.getBody(info))
                            print('\nReporte Generado\n')
                        else:
                            print('\nNo Se Ha Cargado Data\n')
                    except:
                        print('\nHa Ocurrido Un Error Al Generar El Reporte\n')
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